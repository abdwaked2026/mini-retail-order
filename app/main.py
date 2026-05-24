from fastapi import FastAPI

app = FastAPI(title="Mini Retail Order API")


@app.get("/")
def read_root():
    return {"message": "Mini Retail Order API is running"}