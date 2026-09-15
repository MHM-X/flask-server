from flask import Blueprint, jsonify
from app.services.item_service import get_all_items

items_bp = Blueprint("items", __name__)

@items_bp.route("/items", methods=["GET"])
def get_items():
    items = get_all_items()

    return jsonify([
        {
            "id": item.id,
            "name": item.name,
            "servicePrices": item.servicePrices,
            "name_in_english": item.name_in_english
        }
        for item in items
    ])