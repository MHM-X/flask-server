from app.models.item import Item

def get_all_items():
    return Item.query.all()