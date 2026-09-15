from app.extensions import db

class User(db.Model):
    __tablename__ = "users"

    uid=db.Column(db.Uuid, primary_key=True)
    name=db.Column(db.Text)
    role = db.Column(db.Text, default="customer")
    has_active_order = db.Column(db.Boolean)
    email = db.Column(db.Text)
    phone = db.Column(db.Text)