from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Starter",
    version="1.0.0",
    description="A production-ready FastAPI starter template."
)

@app.get("/")
def root():
    return {
        "message": "Welcome to FastAPI Starter"
    }
