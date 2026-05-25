# Mini Retail Order (MRO) 

A small ERP-style retail ordering portal built with **FastAPI**, **SQLite**, **vanilla JavaScript**, and a **shadcn-inspired UI**.

This project simulates a simple business workflow where customers submit custom product orders and an admin team manages order statuses through a dashboard.

## Why I Built This

I built this project to demonstrate practical junior developer skills for business-system and portal development.

The project focuses on:

- Python backend development with FastAPI
- SQLite database design
- Vanilla HTML, CSS, and JavaScript
- Customer-facing order forms
- Admin dashboard workflows
- SQL JOIN queries
- Clean documentation and Git workflow


## Build MRO portal
### 1- Create MRO environment
- Create the project folder
```bash
mkdir mini-retail-order
cd mini-retail-order
```
- Create and activate the virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```
- create a README file 
```bash
type nul > README.md
```
---
### 2- Add Basic Project Files Before Connecting to GitHub

Create the basic files needed for the project.

- Create a `.gitignore` file:

```bash
type nul > .gitignore
```

- Open the `.gitignore` file and add this content:

```gitignore
.venv/
__pycache__/
*.pyc
.env
.DS_Store
```

- Create the main Python file:

```bash
mkdir app
type nul > app\main.py
```
- Add a simple test code inside `main.py`:
```python
print("Mini Retail Order project is running!")
```

- Run the Python file to test it:
```bash
python app/main.py
```

You should see:
```bash
Mini Retail Order project is running!
```

---
### 3- Connect the Project to GitHub
- Initialize Git in the project folder:
```bash
git init
```
- Add all project files to Git:
```bash
git add .
```
- Commit the project files:
```bash
git commit -m "Initial project setup"
```
- Rename the main branch to `main`:
```bash
git branch -M main
```
- Connect the local project to the GitHub repository:
```bash
git remote add origin https://github.com/abdwaked2026/mini-retail-order.git
```
- Push the project to GitHub:
```bash
git push -u origin main
```
- Check that the remote repository is connected correctly:

```bash
git remote -v
```
---
### 4- Database (SQLite)
### 4-1 Database GitHub Setup
- Create a new Git branch for the database setup:
```bash
git checkout -b feature/database-setup
```

- Check that you are on the correct branch:
```bash
git status
```
You should see something like:
```text
On branch feature/database-setup
```
### 4-2 Database Setup
- Create the `database` folder:
```bash
mkdir database
```

- Create the database files:
```bash
type nul > database\schema.sql
type nul > database\seed.sql
type nul > database\init_db.py
```

- Create image folder
```bash
mkdir app\static
mkdir app\static\images
```
### 4-3 Database Relationship Diagram

The database has three main tables: `customers`, `products`, and `orders`.

```mermaid
erDiagram
    CUSTOMERS {
        INTEGER id PK "AUTOINCREMENT"
        TEXT name "NOT NULL"
        TEXT email "NOT NULL"
        TEXT company_name "NULL"
        TEXT created_at "DEFAULT CURRENT_TIMESTAMP"
    }

    PRODUCTS {
        INTEGER id PK "AUTOINCREMENT"
        TEXT name "NOT NULL"
        TEXT description "NULL"
        REAL base_price "NOT NULL"
        INTEGER stock_quantity "NOT NULL DEFAULT 0"
        TEXT image_path "NULL"
        TEXT created_at "DEFAULT CURRENT_TIMESTAMP"
    }

    ORDERS {
        INTEGER id PK "AUTOINCREMENT"
        INTEGER customer_id FK "NOT NULL"
        INTEGER product_id FK "NOT NULL"
        TEXT custom_text "NOT NULL"
        INTEGER quantity "NOT NULL"
        TEXT special_instructions "NULL"
        TEXT status "NOT NULL DEFAULT Pending"
        TEXT created_at "DEFAULT CURRENT_TIMESTAMP"
    }

    CUSTOMERS ||--o{ ORDERS : places
    PRODUCTS ||--o{ ORDERS : includes
```

- One customer can place many orders.
- One product can be used in many orders.
- Each order belongs to one customer.
- Each order belongs to one product.
- The `orders` table connects the `customers` table and the `products` table.

### 4-3 Database Execution and Testing
- Build the database
```bash
python database\init_db.py
```

- You should see:
```text
Database created successfully!
Database location: projectPath\mini-retail-order\database\mini_retail_order.db
```
###  4-5 Exclude Database Files in `.gitignore`
- Add these lines to the `.gitignore` file:
```text
*.db
*.sqlite
*.sqlite3
```
### 4-6 Push Database Setup to GitHub

- Check that you are on the database branch:

```bash
git status
```

You should see:

```text
On branch feature/database-setup
```

- Add the database setup files to Git:

```bash
git add .
```

- Commit the database setup:

```bash
git commit -m "Add SQLite database setup"
```

- Push the database branch to GitHub:

```bash
git push -u origin feature/database-setup
```

- Check that everything is pushed:

```bash
git status
```

You should see:

```text
nothing to commit, working tree clean
```

---

### 4-7 Update Local Main Branch After Merging Pull Request

After you merge the pull request on GitHub, update your local `main` branch.

- Switch back to the `main` branch:

```bash
git checkout main
```

- Update the local `main` branch to match GitHub:

```bash
git pull origin main
```

- Check that your local `main` branch is clean:

```bash
git status
```

You should see:

```text
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

---
### 5- Backend Setup with FastAPI
### 5-1 Backend GitHub Setup
- Create a new Git branch for the backend setup:

```bash
git checkout -b feature/backend-setup
git status
```
### 5-2 Install Backend Dependencies
- Create the `requirements.txt` file:
```bash
type nul > requirements.txt
```

- Open `requirements.txt` and add these libraries:
```text
fastapi==0.136.1
uvicorn==0.47.0
```

- Install the libraries from `requirements.txt`:
```bash
pip install -r requirements.txt
```

- Check that the libraries were installed:
```bash
pip list
```

### 5-3 Create Backend Files
- Create the backend files:
```bash
type nul > app\database.py
type nul > app\models.py
```

- Create the routes folder:
```bash
mkdir app\routes
```

- Create route files:
```bash
type nul > app\routes\products.py
type nul > app\routes\customers.py
type nul > app\routes\orders.py
```
---
### 5-4 Run the FastAPI Backend
> **Note:**  
> The `app/main.py` file contains the starter FastAPI code. This code creates the API app and adds a basic `/` route to test that the backend is running.
- Run the backend server:
```bash
uvicorn app.main:app --reload
```

- Open the API in the browser:
```text
http://127.0.0.1:8000
```

- Open the automatic API documentation:
```text
http://127.0.0.1:8000/docs
```
### 5-5 Save and Push Backend Setup

After testing that the FastAPI server works, save the backend setup changes with Git.

```bash
git add app\main.py app\database.py app\models.py app\routes\products.py app\routes\customers.py app\routes\orders.py requirements.txt README.MD
git commit -m "Set up FastAPI backend starter"
git push -u origin feature/backend-setup
git checkout main
git pull origin main
```

### 5-6 Connect FastAPI with SQLite
In this step, FastAPI is connected to the local SQLite database. The database path is stored in a `.env` file so the path can be changed later without editing the Python code.

#### 5-6-1 Create a new branch

Create a new branch for the SQLite connection work:

```bash
git checkout -b feature/connect-sqlite
```

#### 5-6-2 Create a .env file for database configuration
This project uses a local `.env` file for configuration.

- Create a `.env` file:
```bash
type nul > .env
```
- open `.env` and add
```text
DATABASE_PATH=database/mini_retail_order.db
```
#### 5-6-4 Create a .env.example file for GitHub
```bash
type nul > .env.example
```
- open `.env.example` and add
```text
DATABASE_PATH=database/mini_retail_order.db
```
- Add .env in .gitignore

#### 5-6-5 Install python-dotenv
- Add this package `python-dotenv==1.2.1` to requirements.txt 
```bash
pip install -r requirements.txt
```

#### 5-6-6 Update `app/database.py`
Change the Database connection path

#### 5-6-7 Add a database test route `app/main.py`
This route checks that FastAPI can connect to SQLite and read the database tables.

#### 5-6-8 Test the connection
- Run the FastAPI server
```bash
uvicorn app.main:app --reload
http://127.0.0.1:8000/db-test
```
- Expected result:
```text
{
  "message": "Database connection successful",
  "tables": [
    "customers",
    "sqlite_sequence",
    "products",
    "orders"
  ]
}
```
#### 5-6-9 Save and push changes
After testing that the connection works, save the changes with Git
```bash
git status
git add .gitignore README.MD app\database.py app\main.py requirements.txt .env.example
git commit -m "Connect FastAPI to SQLite database"
git push -u origin feature/connect-sqlite
git checkout main
git pull origin main
```

### 5-7 Create GET /products Route
- Create a new branch
```bash
git checkout -b feature/products-route
```

- Update `app/routes/products.py`
```text
router = APIRouter(prefix="/products", tags=["Products"])
```
- Update `app/main.py`
```text
from app.routes import products
app.include_router(products.router)
```

- Run and test
```bash
uvicorn app.main:app --reload
http://127.0.0.1:8000/products/
```

- Output expected:
```text
[
  {
    "id": 1,
    "name": "Custom Mug",
    "description": "Personalized ceramic mug with custom text.",
    "base_price": 12.99,
    "stock": 50
  },
  {
    "id": 2,
    "name": "Custom T-Shirt",
    "description": "Cotton t-shirt with printed custom design.",
    "base_price": 24.99,
    "stock": 30
  },
  {
    "id": 3,
    "name": "Custom Notebook",
    "description": "Personalized notebook for school or office use.",
    "base_price": 9.99,
    "stock": 100
  }
]
```
- push to GitHub
```bash
git add README.MD app\main.py app\routes\products.py
git commit -m "Add products API route"
git push -u origin feature/products-route
```

---

### 5-8 Create GET /customers/ Route
- Update local main
```bash
git checkout main
git pull origin main
```

- Create a new branch
```bash
git checkout -b feature/customers-route
```

- Update `app/routes/customers.py`
```text
router = APIRouter(prefix="/customers", tags=["Customers"])
```
- Update `app/main.py`
```text
from app.routes import customers, products
app.include_router(customers.router)
```

- Run and test
```bash
uvicorn app.main:app --reload
http://127.0.0.1:8000/customers/
```

- Output expected:
```text
[
  {
    "id": 1,
    "name": "Bob Alex",
    "email": "bob@example.com",
    "company_name": "Bob Designs",
    "created_at": "2026-05-24 12:53:10"
  },
  {
    "id": 2,
    "name": "Omar Ali",
    "email": "omar@example.com",
    "company_name": "Omar Retail Co.",
    "created_at": "2026-05-24 12:53:10"
  },
  {
    "id": 3,
    "name": "Sara John",
    "email": "sara@example.com",
    "company_name": null,
    "created_at": "2026-05-24 12:53:10"
  }
]
```
- push to GitHub
```bash
git add README.MD app\main.py app\routes\customers.py
git commit -m "Add customers API route"
git push -u origin feature/customers-route
```

### 5-9 Create GET /orders/ Route
- Update local main
```bash
git checkout main
git pull origin main
```

- Create a new branch
```bash
git checkout -b feature/orders-route
```

- Update `app/routes/orders.py`
```text
router = APIRouter(prefix="/orders", tags=["Orders"])
```
- Update `app/main.py`
```text
from app.routes import customers, products, orders
app.include_router(orders.router)
```

- Run and test
```bash
uvicorn app.main:app --reload
http://127.0.0.1:8000/orders/
```

- Output expected:
```text
[
  {
    "id": 1,
    "customer_id": 1,
    "product_id": 1,
    "custom_text": "Best Teacher Ever",
    "quantity": 2,
    "special_instructions": "Use blue text if possible.",
    "status": "Pending",
    "created_at": "2026-05-24 12:53:10"
  },
  {
    "id": 2,
    "customer_id": 2,
    "product_id": 2,
    "custom_text": "Omar Retail Team",
    "quantity": 5,
    "special_instructions": "Need all shirts in size medium.",
    "status": "Processing",
    "created_at": "2026-05-24 12:53:10"
  },
  {
    "id": 3,
    "customer_id": 3,
    "product_id": 3,
    "custom_text": "Sara Notes",
    "quantity": 3,
    "special_instructions": null,
    "status": "Completed",
    "created_at": "2026-05-24 12:53:10"
  }
]
```
- push to GitHub
```bash
git add app\main.py app\routes\orders.py README.MD
git commit -m "Add orders API route"
git push -u origin feature/orders-route
```

### 5-10 Improve GET /orders/ with JOIN
- Update local main
```bash
git checkout main
git pull origin main
```

- Create a new branch
```bash
git checkout -b feature/orders-details-route
```

- Update `app/routes/orders.py`
```text
change select statement with JOIN
```
- Run and test
```bash
uvicorn app.main:app --reload
http://127.0.0.1:8000/orders/
```

- Output expected:
```text
[
  {
    "id": 1,
    "customer_name": "Bob Alex",
    "product_name": "Custom Mug",
    "quantity": 2,
    "base_price": 12.99,
    "total_price": 25.98
  },
  {
    "id": 2,
    "customer_name": "Omar Ali",
    "product_name": "Custom T-Shirt",
    "quantity": 5,
    "base_price": 24.99,
    "total_price": 124.95
  },
  {
    "id": 3,
    "customer_name": "Sara John",
    "product_name": "Custom Notebook",
    "quantity": 3,
    "base_price": 9.99,
    "total_price": 29.97
  }
]
```
- push to GitHub
```bash
git add app\routes\orders.py README.MD
git commit -m "Improve orders route with customer and product details"
git push -u origin feature/orders-details-route
```
### 6- Frontend setup