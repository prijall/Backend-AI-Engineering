from fastapi import FastAPI
from api import router
import uvicorn


app = FastAPI(title="Simple Backend Server")

app.include_router(router)


if __name__=="__main__":
    uvicorn.run("Week_1.main_week1:app", host="localhost", port=8000, reload=True)