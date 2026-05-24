from fastapi import FastAPI
from app.database import get_db_connection
from app.routes import products,customers

app = FastAPI(title="Mini Retail Order API")
app.include_router(products.router)
app.include_router(customers.router)
# Test endpoint to verify that the API is running
@app.get("/")
def read_root():
    return {"message": "Mini Retail Order API is running"}


# Test endpoint to verify database connection and list tables
@app.get("/db-test")
def test_database_connection():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    connection.close()

    return {
        "message": "Database connection successful",
        "tables": [table["name"] for table in tables],
    }