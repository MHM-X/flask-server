from app import create_app


def test_get_items():
    app = create_app()
    client = app.test_client()

    response = client.get("/items")

    assert response.status_code == 200
    assert response.is_json

    data = response.get_json()

    assert isinstance(data, list)
