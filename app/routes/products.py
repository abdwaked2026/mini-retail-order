from fastapi import APIRouter

from app.database import get_db_connection

router = APIRouter(prefix="/products", tags=["Products"])

# Endpoint to get the list of all products
@router.get("/")
def get_products():
    connection = get_db_connection()
    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, description,base_price,stock_quantity stock FROM products;")
    products = cursor.fetchall()

    connection.close()
    # Convert the list of sqlite3.Row objects to a list of dictionaries for better JSON serialization
    return [dict(product) for product in products]