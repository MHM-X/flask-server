from flask import Blueprint, jsonify, request
from app.services.order_service import get_current_orders, create_order


orders_bp = Blueprint("orders", __name__)


@orders_bp.route("/orders/<uid>", methods=["GET"])
def get_orders(uid):
    try:
        orders = get_current_orders(uid)

        return jsonify([
            {
                "id": order.id,
                "created_at": order.created_at.isoformat(),
                "items": order.items,
                "status": order.status,
                "subtotal": order.subtotal,
                "delivery_fee": order.delivery_fee,
                "total": order.total,
                "customer_id": order.customer_id,
                "notes": order.notes,
                "time_interval": order.time_interval
            }
            for order in orders
        ])

    except Exception as e:
       print(e)

    return jsonify({
        "error": "Failed to fetch orders"
    }), 500

@orders_bp.route("/orders", methods=["POST"])
def add_order():
    try:
        data = request.get_json()

        order = create_order(
            id=data["id"],
            created_at=data["created_at"],
            items=data["items"],
            status=data["status"],
            subtotal=data["subtotal"],
            delivery_fee=data["delivery_fee"],
            total=data["total"],
            customer_id=data["customer_id"],
            notes=data["notes"],
            time_interval=data["time_interval"]
        )

        return jsonify({
            "id": order.id,
            "message": "Order created successfully"
        }), 201

    except KeyError as e:
        return jsonify({
            "error": f"Missing required field: {e.args[0]}"
        }), 400

    except Exception:
        return jsonify({
            "error": "Failed to create order"
        }), 500