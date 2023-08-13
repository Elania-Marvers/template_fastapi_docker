from sqlalchemy.orm import Session
from models.item_model import Item

def create_default_items(db: Session):
    print("Creating default items")
    default_items = ["Item A", "Item B", "Item C"]
    
    for item_name in default_items:
        if db.query(Item).filter(Item.name == item_name).first() is None:
            db_item = Item(name=item_name)
            db.add(db_item)
            db.commit()
