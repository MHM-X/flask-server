from app.extensions import db
from sqlalchemy.dialects.postgresql import JSONB


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True))
    items = db.Column(JSONB)
    status = db.Column(db.Text)
    subtotal = db.Column(db.Float)
    delivery_fee = db.Column(db.Float)
    total = db.Column(db.Float)
    customer_id = db.Column(db.Text)
    notes = db.Column(db.Text)
    time_interval = db.Column(db.BigInteger)