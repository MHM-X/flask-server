from app import create_app
from app.extensions import db
from app.models.item import Item
from app.models.order import Order
from app.models.user import User


def test_get_items():
    app = create_app()

    with app.app_context():
        db.create_all()

    client = app.test_client()

    response = client.get("/items")

    assert response.status_code == 200
    assert response.is_json

    data = response.get_json()

    assert isinstance(data, list)
