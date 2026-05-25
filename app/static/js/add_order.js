const customerSelect = document.getElementById("customer_id");
const productSelect = document.getElementById("product_id");
const orderForm = document.getElementById("add-order-form");
const messageBox = document.getElementById("message");

/**
 * Load customers from the backend and populate the customer dropdown.
 * This function is called when the page loads to ensure the dropdown is populated with current customers.
 */
async function loadCustomers() {
    try {
        const response = await fetch("/customers/");

        if (!response.ok) {
            throw new Error("Failed to load customers.");
        }

        const customers = await response.json();

        customerSelect.innerHTML = '<option value="">Select a customer</option>';

        customers.forEach((customer) => {
            const option = document.createElement("option");
            option.value = customer.id;

            option.textContent = `${customer.name} (${customer.email})`;

            customerSelect.appendChild(option);
        });
    } catch (error) {
        customerSelect.innerHTML = '<option value="">Could not load customers</option>';
        showMessage(error.message, "error");
    }
}

/**
 * Load products from the backend and populate the product dropdown.
 * This function is called when the page loads to ensure the dropdown is populated with current products.
 */
async function loadProducts() {
    try {
        const response = await fetch("/products/");

        if (!response.ok) {
            throw new Error("Failed to load products.");
        }

        const products = await response.json();

        productSelect.innerHTML = '<option value="">Select a product</option>';

        products.forEach((product) => {
            const option = document.createElement("option");
            option.value = product.id;

            option.textContent = `${product.name} - $${product.base_price} | Stock: ${product.stock_quantity}`;

            productSelect.appendChild(option);
        });
    } catch (error) {
        productSelect.innerHTML = '<option value="">Could not load products</option>';
        showMessage(error.message, "error");
    }
}

/**
 * Handle the form submission for creating a new order.
 * This function is called when the user submits the order form.
 */
orderForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const orderData = {
        customer_id: Number(customerSelect.value),
        product_id: Number(productSelect.value),
        custom_text: document.getElementById("custom_text").value,
        quantity: Number(document.getElementById("quantity").value),
        special_instructions: document.getElementById("special_instructions").value || null,
    };

    try {
        const response = await fetch("/orders/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(orderData),
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.detail || "Failed to create order.");
        }

        showMessage(`Order created successfully! Order ID: ${result.order_id}`, "success");

        orderForm.reset();

        await loadProducts();
    } catch (error) {
        showMessage(error.message, "error");
    }
});

/**
 * Display a message to the user.
 * This function is called to show success or error messages after form submission.
 */
function showMessage(message, type) {
    messageBox.textContent = message;
    messageBox.className = `message ${type}`;
}

loadCustomers();
loadProducts();