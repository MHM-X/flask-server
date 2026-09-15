from app.extensions import db
from sqlalchemy.dialects.postgresql import JSONB

class Item(db.Model):
    __tablename__="items"
    id=db.Column(db.BigInteger, primary_key=True)
    name=db.Column(db.Text)
    servicePrices=db.Column(JSONB)
    name_in_english=db.Column(db.Text)