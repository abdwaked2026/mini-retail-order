const ordersContainer = document.getElementById("orders-container");
const orderIdInput = document.getElementById("order-id-input");
const searchButton = document.getElementById("search-order-button");
const loadAllButton = document.getElementById("load-all-button");
const messageBox = document.getElementById("message");

/**
 * Load all orders from the backend.
 * This function is called when the page loads or when the user clicks the "Load All" button.
 */
async function loadAllOrders() {
    clearMessage();
    ordersContainer.innerHTML = "<p>Loading orders...</p>";

    try {
        const response = await fetch("/orders/");

        if (!response.ok) {
            throw new Error("Failed to load orders.");
        }

        const orders = await response.json();

        displayOrders(orders);
    } catch (error) {
        ordersContainer.innerHTML = "";
        showMessage(error.message, "error");
    }
}

/**
 * Search for an order by its ID.
 * This function is called when the user clicks the search button.
 */
async function searchOrderById() {
    clearMessage();

    const orderId = orderIdInput.value;

    if (!orderId) {
        showMessage("Please enter an order ID.", "error");
        return;
    }

    ordersContainer.innerHTML = "<p>Searching...</p>";

    try {
        const response = await fetch(`/orders/${orderId}`);

        const order = await response.json();

        if (!response.ok) {
            throw new Error(order.detail || "Order not found.");
        }

        displayOrders([order]);
    } catch (error) {
        ordersContainer.innerHTML = "";
        showMessage(error.message, "error");
    }
}

/**
 * Display a list of orders in the UI.
 * This function is called to show the loaded orders.
 */
function displayOrders(orders) {
    if (!orders || orders.length === 0) {
        ordersContainer.innerHTML = "<p>No orders found.</p>";
        return;
    }

    ordersContainer.innerHTML = "";

    orders.forEach((order) => {
        const orderCard = document.createElement("div");
        orderCard.className = "order-card";

        orderCard.innerHTML = `
            <h3>Order #${order.id}</h3>

            <p><strong>Customer:</strong> ${order.customer_name || order.customer_id}</p>
            <p><strong>Product:</strong> ${order.product_name || order.product_id}</p>
            <p><strong>Custom Text:</strong> ${order.custom_text}</p>
            <p><strong>Quantity:</strong> ${order.quantity}</p>
            <p><strong>Status:</strong> ${order.status}</p>
            <p><strong>Special Instructions:</strong> ${order.special_instructions || "None"}</p>
            <p><strong>Created At:</strong> ${order.created_at}</p>
        `;

        ordersContainer.appendChild(orderCard);
    });
}

/**
 * Display a message to the user.
 * This function is called to show success or error messages.
 */
function showMessage(message, type) {
    messageBox.textContent = message;
    messageBox.className = `message ${type}`;
}

/**
 * Clear any existing messages.
 * This function is called to remove previous messages.
 */ 
function clearMessage() {
    messageBox.textContent = "";
    messageBox.className = "message";
}

searchButton.addEventListener("click", searchOrderById);
loadAllButton.addEventListener("click", loadAllOrders);

loadAllOrders();