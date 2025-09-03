📦 Inventory Management System

A simple Flask + HTML/CSS/JS based Inventory Management System.

It allows you to:
✅ Add products with SKU, name, stock, and price
✅ View all products in a table
✅ Record sales (reduces stock automatically)
✅ See updated stock in real-time

📂 Project Structure
Final_Project/
│
├── app.py # Flask backend (API + DB Models + Routes)
├── inventory.db # SQLite database (auto-created)
│
├── static/ # Frontend (served by Flask)
│ ├── index.html # Main UI
│ ├── style.css # Styling
│ └── script.js # API integration
│
└── README.md # Documentation

⚙️ Backend (Flask)
🏗 Models

Product

id (int) – Product ID

sku (string) – Unique SKU

name (string) – Product name

price (decimal) – Price per unit

stock (int) – Current stock

created_at (datetime)

Sale

id (int) – Sale ID

product_id (FK → Product)

quantity (int)

unit_price (decimal)

total_price (decimal)

sold_at (datetime)

🔑 API Endpoints
Method Endpoint Description
POST /products Add a new product
GET /products List all products
POST /sales Record a sale (updates stock)
🎨 Frontend (HTML + CSS + JS)
Features

Add Product Form
Inputs SKU, Name, Stock, Price → sends POST /products

Record Sale Form
Inputs Product ID + Quantity → sends POST /sales

Product Table
Auto-fetches from GET /products and displays in a table

📜 Functions in script.js

fetchProducts() → Gets all products and updates the table

addProduct() → Adds product via API, refreshes list

recordSale() → Records sale, updates stock

window.onload = fetchProducts; → Loads products on page open

▶️ How to Run

1. Clone the repository
   git clone <repo-url>
   cd Final_Project

2. Install dependencies
   pip install flask flask_sqlalchemy

3. Run backend
   python app.py

Flask will run at:
👉 http://127.0.0.1:5000

4. Open frontend

In browser, go to:
👉 http://127.0.0.1:5000/static/index.html

📊 Example Workflow

Add Product:

SKU = SKU001

Name = Laptop

Stock = 10

Price = 800

Product shows in table.

Record Sale:

Product ID = 1

Quantity = 2

→ Stock decreases automatically.

🚀 Future Improvements

Delete products

Edit product details

Sales history page

Low-stock alert report

Dashboard summary

✅ Summary:
This project demonstrates a CRUD-like Inventory Management System using Flask backend and a vanilla JS frontend.
It covers:

REST API design

Database with SQLAlchemy

API integration with Fetch

Real-time updates to UI
