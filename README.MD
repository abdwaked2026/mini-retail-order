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
### 5- Backend setup

---
### 6- Frontend setup