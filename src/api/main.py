"""RANTE API"""

# FastAPI
from fastapi import FastAPI

# Routers 
from src.api.routers import openai

app = FastAPI()

app.include_router(openai.router, tags=["openai"], prefix="/openai")
