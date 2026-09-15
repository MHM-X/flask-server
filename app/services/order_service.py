from app.models.order import Order
from app.extensions import db

def get_current_orders(uid):
    return Order.query.filter_by(customer_id=str(uid)).all()


def create_order(
    id,
    created_at,
    items,
    status,
    subtotal,
    delivery_fee,
    total,
    customer_id,
    notes,
    time_interval
):
    order = Order(
        id=id,
        created_at=created_at,
        items=items,
        status=status,
        subtotal=subtotal,
        delivery_fee=delivery_fee,
        total=total,
        customer_id=customer_id,
        notes=notes,
        time_interval=time_interval
    )

    db.session.add(order)
    db.session.commit()

    return order