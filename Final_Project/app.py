from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS

app = Flask(__name__)

# Database config: default sqlite, can override with MySQL by setting INVENTORY_DATABASE_URL
DATABASE_URL = os.environ.get("INVENTORY_DATABASE_URL") or "sqlite:///inventory.db"
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# MODELS
class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(64), unique=True, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)  # unit price
    stock = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def as_dict(self):
        return {
            "id": self.id,
            "sku": self.sku,
            "name": self.name,
            "price": float(self.price),
            "stock": self.stock,
            "created_at": self.created_at.isoformat(),
        }


class Sale(db.Model):
    __tablename__ = "sales"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Numeric(10, 2), nullable=False)
    total_price = db.Column(db.Numeric(12, 2), nullable=False)
    sold_at = db.Column(db.DateTime, default=datetime.utcnow)

    product = db.relationship("Product")

    def as_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "product_name": self.product.name if self.product else None,
            "quantity": self.quantity,
            "unit_price": float(self.unit_price),
            "total_price": float(self.total_price),
            "sold_at": self.sold_at.isoformat(),
        }


# Initialize database safely
with app.app_context():
    db.create_all()


# ROUTES

# Add product
@app.route("/products", methods=["POST"])
def add_product():
    data = request.json or {}
    sku = data.get("sku")
    name = data.get("name")
    price = data.get("price")
    stock = data.get("stock", 0)

    if not sku or not name or price is None:
        return jsonify({"error": "sku, name and price are required"}), 400

    if Product.query.filter_by(sku=sku).first():
        return jsonify({"error": "Product with this SKU already exists"}), 400

    p = Product(sku=sku, name=name, price=price, stock=int(stock))
    db.session.add(p)
    db.session.commit()
    return jsonify(p.as_dict()), 201


# List products
@app.route("/products", methods=["GET"])
def list_products():
    q = Product.query.order_by(Product.name.asc()).all()
    return jsonify([p.as_dict() for p in q])


# Record a sale (reduces stock atomically)
@app.route("/sales", methods=["POST"])
def record_sale():
    data = request.json or {}
    product_id = data.get("product_id")
    quantity = int(data.get("quantity", 0))

    if not product_id or quantity <= 0:
        return jsonify({"error": "product_id and positive quantity are required"}), 400

    p = Product.query.get(product_id)
    if not p:
        return jsonify({"error": "Product not found"}), 404

    if quantity > p.stock:
        return jsonify({"error": "Insufficient stock", "available": p.stock}), 400

    unit_price = p.price
    total_price = float(unit_price) * quantity

    # update stock and add sale
    p.stock -= quantity
    sale = Sale(
        product_id=product_id,
        quantity=quantity,
        unit_price=unit_price,
        total_price=total_price,
    )
    db.session.add(sale)
    db.session.commit()
    return jsonify(sale.as_dict()), 201


# Sales history
@app.route("/sales", methods=["GET"])
def list_sales():
    q = Sale.query.order_by(Sale.sold_at.desc()).limit(200).all()
    return jsonify([s.as_dict() for s in q])


if __name__ == "__main__":
    # For development only
    app.run(debug=True, host="127.0.0.1", port=5500)
CORS(app)