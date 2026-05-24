import sqlite3
from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / os.getenv("DATABASE_PATH", "database/mini_retail_order.db")



def get_db_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection