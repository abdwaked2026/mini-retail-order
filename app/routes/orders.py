from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from app.database import get_db_connection

router = APIRouter(prefix="/orders", tags=["Orders"])

class OrderCreate(BaseModel):
    customer_id: int
    product_id: int
    custom_text: str
    quantity: int
    special_instructions: str | None = None
    
# Endpoint to get all orders
@router.get("/")
def get_orders():
    connection = get_db_connection()
    cursor = connection.cursor()

    # For test
    #cursor.execute("SELECT * FROM orders;")
    # With Join to get customer name and product name
    cursor.execute(
        """
        SELECT
            orders.id,
            customers.name AS customer_name,
            products.name AS product_name,
            orders.quantity,
            products.base_price,
            orders.quantity * products.base_price AS total_price
        FROM orders
        JOIN customers ON orders.customer_id = customers.id
        JOIN products ON orders.product_id = products.id;
        """
    )
    orders = cursor.fetchall()

    connection.close()

    return [dict(order) for order in orders]

# Endpoint to create a new order
@router.post("/")
def create_order(order: OrderCreate):
    if order.quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than 0")

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM customers WHERE id = ?;", (order.customer_id,))
    customer = cursor.fetchone()

    if customer is None:
        connection.close()
        raise HTTPException(status_code=404, detail="Customer not found")

    cursor.execute("SELECT * FROM products WHERE id = ?;", (order.product_id,))
    product = cursor.fetchone()

    if product is None:
        connection.close()
        raise HTTPException(status_code=404, detail="Product not found")

    if product["stock_quantity"] < order.quantity:
        connection.close()
        raise HTTPException(status_code=400, detail="Not enough stock available")

    cursor.execute(
        """
        INSERT INTO orders (
            customer_id,
            product_id,
            custom_text,
            quantity,
            special_instructions,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?);
        """,
        (
            order.customer_id,
            order.product_id,
            order.custom_text,
            order.quantity,
            order.special_instructions,
            "pending",
        ),
    )

    new_order_id = cursor.lastrowid

    cursor.execute(
        """
        UPDATE products
        SET stock_quantity = stock_quantity - ?
        WHERE id = ?;
        """,
        (order.quantity, order.product_id),
    )

    connection.commit()
    connection.close()

    return {
        "message": "Order created successfully",
        "order_id": new_order_id,
        "customer_id": order.customer_id,
        "product_id": order.product_id,
        "custom_text": order.custom_text,
        "quantity": order.quantity,
        "special_instructions": order.special_instructions,
        "status": "pending",
    }