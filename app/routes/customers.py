from fastapi import APIRouter

from app.database import get_db_connection

router = APIRouter(prefix="/customers", tags=["Customers"])

# Endpoint to get all customers
@router.get("/")
def get_customers():
    connection = get_db_connection()
    # Use a cursor to execute SQL queries and fetch results
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM customers;")
    customers = cursor.fetchall()

    connection.close()
    # Convert the list of sqlite3.Row objects to a list of dictionaries for better JSON serialization
    return [dict(customer) for customer in customers]