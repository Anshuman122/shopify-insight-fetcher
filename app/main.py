from fastapi import FastAPI
from app.routers import fetch

app = FastAPI()

# Include router
app.include_router(fetch.router)
