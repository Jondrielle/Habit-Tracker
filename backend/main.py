from fastapi import FastAPI
from routes.habits import router
from fastapi.middleware.cors import CORSMiddleware

origins =[
	
]

app = FastAPI()



app.include_router(router)