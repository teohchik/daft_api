from fastapi import FastAPI
from app.api.endpoints import cookies

app = FastAPI(title="Cookie Transformer API")

# Include API routes
app.include_router(cookies.router, tags=["cookies"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)