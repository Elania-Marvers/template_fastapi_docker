from fastapi import FastAPI
from item_routes import router as item_router
from item_model import Base
from database import engine

app = FastAPI()

app.include_router(item_router, tags=["items"])

Base.metadata.create_all(bind=engine)
