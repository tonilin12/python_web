from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import Form
from pathlib import Path
from .routes import router
from .routes import *
import requests

app = FastAPI()

app.include_router(router, tags=["Event"])

@app.get("/", tags=["Root"])
async def read_root():
    return("welcome to this wonderful page")
