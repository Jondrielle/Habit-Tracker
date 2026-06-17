from fastapi import FastAPI
from routes.habits import router


app = FastAPI()


app.include_router(router)