import streamlit as st
import json
import os
from collections import Counter, defaultdict
from datetime import datetime, timedelta
import data_generator as dg
import random

st.header("Data Setup")

if st.button('Generate Synthetic Orders'):
    dg.generate_orders(random.randint(4000, 5000))
    st.success("Data Generated Successfully!")
else:
    st.write('Waiting for data...')
    st.error("No data available. Click the button in the sidebar to generate orders.")
    st.stop()

def load_data():
    with open("orders.json", "r") as f:
        data = json.load(f)
    for order in data:
        order["order_date"] = datetime.fromisoformat(order["order_date"])
    return data

orders = load_data()


total_orders = len(orders)
delivered_orders = [o for o in orders if o["order_status"] == "delivered"]
total_revenue = sum(o["order_amount"] for o in delivered_orders)
average_order_value = total_revenue / len(delivered_orders) if delivered_orders else 0


product_counter = Counter()
for o in orders:
    for item in o["items"]:
        product_counter[item["name"]] += item["qty"]

most_popular = product_counter.most_common(1)[0]


cancelled_orders = len([o for o in orders if o["order_status"] == "cancelled"])
cancellation_rate = (cancelled_orders / total_orders) * 100


last_7_days = [datetime.now().date() - timedelta(days=i) for i in range(7)]
revenue_by_day = {day: 0 for day in last_7_days}
for o in delivered_orders:
    o_day = o["order_date"].date()
    if o_day in revenue_by_day:
        revenue_by_day[o_day] += o["order_amount"]


user_spending = defaultdict(float)
for o in delivered_orders:
    user_spending[o["user_id"]] += o["order_amount"] 
top_users = sorted(user_spending.items(), key=lambda x: x[1], reverse=True)[:5]
total_users = sorted(user_spending.items(), key=lambda x: x[0], reverse=False)[:]