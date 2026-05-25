from fastapi import APIRouter

from app.database import get_db_connection

router = APIRouter(prefix="/orders", tags=["Orders"])

# Endpoint to get all orders
@router.get("/")
def get_orders():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM orders;")
    orders = cursor.fetchall()

    connection.close()

    return [dict(order) for order in orders]