import json
import random
from datetime import datetime, timedelta

PRODUCTS = [
    {"name": "T-shirt", "price": 499},
    {"name": "Jeans", "price": 1199},
    {"name": "Shoes", "price": 1799},
    {"name": "Watch", "price": 999},
    {"name": "Backpack", "price": 899}
]

ORDER_STATUSES = ["delivered", "cancelled", "returned", "pending"]

def generate_order():
    order_id = "ORD" + str(random.randint(10000, 99999))
    user_id = "U" + str(random.randint(100, 999))
    num_items = random.randint(1, 3)
    items = []
    order_amount = 0

    for _ in range(num_items):
        product = random.choice(PRODUCTS)
        qty = random.randint(1, 4)
        item_total = product["price"] * qty
        items.append({
            "name": product["name"],
            "qty": qty,
            "price": product["price"]
        })
        order_amount += item_total

    order_status = random.choices(
        ORDER_STATUSES, weights=[0.7, 0.15, 0.1, 0.05], k=1)[0]

    order_date = datetime.now() - timedelta(days=random.randint(0, 30),
                                            hours=random.randint(0, 23),
                                            minutes=random.randint(0, 59))

    return {
        "order_id": order_id,
        "user_id": user_id,
        "order_amount": round(order_amount, 2),
        "items": items,
        "order_status": order_status,
        "order_date": order_date.isoformat()
    }

def generate_orders(n):
    orders = [generate_order() for _ in range(n)]
    with open("orders.json", "w") as f:
        json.dump(orders, f, indent=2)