from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.basket_model import Basket, BasketCreate
from database import get_db

router = APIRouter()

@router.post("/baskets/")
def create_basket(basket: BasketCreate, db: Session = Depends(get_db)):
    db_basket = Basket(name=basket.name)
    db.add(db_basket)
    db.commit()
    db.refresh(db_basket)
    return db_basket

@router.get("/baskets/{basket_id}")
def read_basket(basket_id: int, db: Session = Depends(get_db)):
    basket = db.query(Basket).filter(Basket.id == basket_id).first()
    return basket

@router.get("/baskets/")
def read_baskets(db: Session = Depends(get_db)):
    baskets = db.query(Basket).all()
    return baskets
