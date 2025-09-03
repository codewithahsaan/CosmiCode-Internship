const API = "http://127.0.0.1:5500"; // Flask backend URL

// Fetch all products
async function fetchProducts() {
  try {
    const res = await fetch(`${API}/products`);
    if (!res.ok) throw new Error(`Error ${res.status}`);
    const data = await res.json();

    const table = document.getElementById("productTable");
    table.innerHTML = "";
    data.forEach((p) => {
      table.innerHTML += `
        <tr>
          <td>${p.id}</td>
          <td>${p.sku}</td>
          <td>${p.name}</td>
          <td>${p.stock}</td>
          <td>$${p.price}</td>
        </tr>`;
    });
  } catch (err) {
    console.error("Fetch products failed:", err);
    alert("Failed to load products.");
  }
}

// Add a new product
async function addProduct() {
  const sku = document.getElementById("psku").value.trim();
  const name = document.getElementById("pname").value.trim();
  const stock = parseInt(document.getElementById("pstock").value);
  const price = parseFloat(document.getElementById("pprice").value);

  if (!sku || !name || isNaN(stock) || isNaN(price)) {
    alert("Please fill all fields correctly.");
    return;
  }

  try {
    const res = await fetch(`${API}/products`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ sku, name, stock, price }),
    });

    if (!res.ok) {
      const errJson = await res.json();
      alert(`Error: ${errJson.error}`);
      return;
    }

    await fetchProducts();
    alert("✅ Product added successfully!");
  } catch (err) {
    console.error("Add product failed:", err);
    alert("Error adding product.");
  }
}

// Record a sale
async function recordSale() {
  const product_id = parseInt(document.getElementById("sid").value);
  const quantity = parseInt(document.getElementById("squantity").value);

  if (isNaN(product_id) || isNaN(quantity)) {
    alert("Please enter valid Product ID and Quantity.");
    return;
  }

  try {
    const res = await fetch(`${API}/sales`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ product_id, quantity }),
    });

    const data = await res.json();
    if (res.ok) {
      alert(`Sale recorded ✅ Total = $${data.total}`);
      fetchProducts();
    } else {
      alert(`Error: ${data.error}`);
    }
  } catch (err) {
    console.error("Record sale failed:", err);
    alert("Error recording sale.");
  }
}

// Load products on page start
window.onload = fetchProducts;
