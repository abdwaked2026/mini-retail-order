from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

# Set up Jinja2 templates to render HTML pages from the "app/templates" directory
templates = Jinja2Templates(directory="app/templates")

router = APIRouter(tags=["Pages"])

# Endpoint to render the "Add Order" page
# http://127.0.0.1:8000/add-order load app/templates/add_order.html

@router.get("/add-order")
def add_order_page(request: Request):
    return templates.TemplateResponse(
        request,
        "add_order.html",
        {"request": request},
    )


# Endpoint to render the "Orders List" page
@router.get("/orders-page")
def orders_page(request: Request):
    return templates.TemplateResponse(
        request,
        "orders.html",
        {"request": request},
    )