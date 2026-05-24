import sqlite3
from pathlib import Path

# Database file paths
BASE_DIR = Path(__file__).resolve().parent
DATABASE_FILE = BASE_DIR / "mini_retail_order.db"   # SQLite database file
SCHEMA_FILE = BASE_DIR / "schema.sql"               # Database structure definition
SEED_FILE = BASE_DIR / "seed.sql"                   # Initial data to populate the database

# Read a SQL file and execute all SQL commands inside it.
def run_sql_file(connection, file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        sql_script = file.read()

    connection.executescript(sql_script)

# Main function to initialize the database
def initialize_database():
    # Step 1: Create or connect to the SQLite database file.
    # If the database file does not exist, SQLite creates an empty database file automatically.
    connection = sqlite3.connect(DATABASE_FILE)

    try:
        # Step 2: Enable foreign key checking for this SQLite connection.
        # This prevents inserting an order with a customer_id or product_id that does not exist.
        # This is required for SQLite.
        # Other databases like MySQL and PostgreSQL usually enforce foreign keys automatically.        connection.execute("PRAGMA foreign_keys = ON;")

        # Step 3: Run schema.sql to create the database tables.
        run_sql_file(connection, SCHEMA_FILE)
        
        # Step 4: Run seed.sql to insert initial sample data into the tables.
        run_sql_file(connection, SEED_FILE)

        # Step 5: Save all changes to the database file.
        connection.commit()

        print("Database created successfully!")
        print(f"Database location: {DATABASE_FILE}")

    except sqlite3.Error as error:
        print("Database error:", error)

    finally:
        # Step 6: Close the database connection.
        connection.close()


if __name__ == "__main__":
    initialize_database()