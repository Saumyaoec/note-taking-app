# app/main.py
from fastapi import FastAPI
from .auth import router as auth_router
from .crud import router as note_router
from .config import MONGODB_CONNECTION_URI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}
app.include_router(auth_router, prefix="/auth")
app.include_router(note_router, prefix="/notes")

# Health check route
@app.get("/ping")
async def ping():
    return {"message": "pong"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



