from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles # For serving static files like CSS and JavaScript
from app.database import get_db_connection
from app.routes import products,customers,orders, pages

app = FastAPI(title="Mini Retail Order API")
# Mount the "app/static" directory to serve static files at the "/static" URL path
app.mount("/static", StaticFiles(directory="app/static"), name="static")


app.include_router(products.router)
app.include_router(customers.router)
app.include_router(orders.router)
app.include_router(pages.router)

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