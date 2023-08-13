from sqlalchemy.orm import Session
from models.basket_model import Basket

def create_default_baskets(db: Session):
    print("Creating default baskets")
    default_baskets = ["Basket A", "Basket B", "Basket C"]
    
    for basket_name in default_baskets:
        if db.query(Basket).filter(Basket.name == basket_name).first() is None:
            db_basket = Basket(name=basket_name)
            db.add(db_basket)
            db.commit()
