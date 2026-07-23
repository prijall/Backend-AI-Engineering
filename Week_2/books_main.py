from fastapi import FastAPI
import uvicorn
from books_api import router


app=FastAPI(title="BOOK Store")
app.include_router(router)
