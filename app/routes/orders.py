from fastapi import APIRouter

from app.database import get_db_connection

router = APIRouter(prefix="/orders", tags=["Orders"])

# Endpoint to get all orders
@router.get("/")
def get_orders():
    connection = get_db_connection()
    cursor = connection.cursor()

    # for test
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