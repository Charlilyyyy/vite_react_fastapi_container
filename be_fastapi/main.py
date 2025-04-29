from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow React frontend to access FastAPI backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to ["http://localhost:5173"] if you want
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple API endpoint
@app.get("/api/hello")
def read_root():
    return {"message": "Hello from FastAPI!"}

# Another sample endpoint (optional)
@app.get("/api/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}
