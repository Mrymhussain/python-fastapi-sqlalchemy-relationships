from fastapi import FastAPI
from controllers.teas import router as TeasRouter
from database import engine
from models.tea import Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(TeasRouter, prefix="/api")


@app.get("/")
def home():
    return {"message": "Home Page"}