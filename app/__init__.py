from flask import Flask
from app.config import Config
from app.extensions import db
from app.routes.items import items_bp
from app.routes.orders import orders_bp
import os



def create_app():
    app=Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(items_bp)

    app.register_blueprint(orders_bp)

    @app.after_request
    def add_backend_header(response):
        response.headers["X-Backend-Server"] = os.getenv(
            "BACKEND_SERVER",
            "unknown"
        )
        return response

    return app