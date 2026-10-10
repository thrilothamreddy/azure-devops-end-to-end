from fastapi import FastAPI

app = FastAPI(title="CloudOps Task API")


@app.get("/")
def home():
    return {"message": "Welcome to CloudOps Task API"}


@app.get("/health")
def health():
    return {"status": "healthy"}