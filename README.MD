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