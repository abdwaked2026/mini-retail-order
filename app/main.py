from fastapi import FastAPI

app = FastAPI(title="Mini Retail Order API")

# Test endpoint to verify that the API is running
@app.get("/")
def read_root():
    return {"message": "Mini Retail Order API is running"}