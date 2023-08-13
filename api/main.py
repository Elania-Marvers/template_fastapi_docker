from fastapi import FastAPI
from routes.item_routes import router as item_router
from routes.basket_routes import router as basket_router
from models.item_model import Base as ItemBase
from models.basket_model import Base as BasketBase
from database import engine, SessionLocal
from utils.item_utils import create_default_items
from utils.basket_utils import create_default_baskets

app = FastAPI()

app.include_router(item_router, tags=["items"])
app.include_router(basket_router, tags=["baskets"])

ItemBase.metadata.create_all(bind=engine)
BasketBase.metadata.create_all(bind=engine)

with SessionLocal() as db:
    create_default_items(db)
    create_default_baskets(db)