from fastapi import FastAPI
from controllers.teas import router as TeasRouter
from database import engine
from models.base import BaseModel


app = FastAPI()

BaseModel.metadata.create_all(bind=engine)

app.include_router(TeasRouter)