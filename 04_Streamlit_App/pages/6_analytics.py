import streamlit as st
import plotly.express as px
from database import run_query

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Analytics Dashboard")
st.markdown("### Business Performance Analytics")
st.divider()

# -----------------------------
# Monthly Revenue
# -----------------------------
monthly = run_query("""
SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(total_amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;
""")

fig = px.bar(
    monthly,
    x="month",
    y="revenue",
    text="revenue",
    title="Monthly Revenue"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# -----------------------------
# Order Status
# -----------------------------
status = run_query("""
SELECT
    order_status,
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_status;
""")

fig = px.pie(
    status,
    names="order_status",
    values="total_orders",
    hole=0.5,
    title="Order Status Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# -----------------------------
# Top Customers
# -----------------------------
st.subheader("👥 Top Customers")

customers = run_query("""
SELECT
    customer_id,
    COUNT(order_id) AS total_orders,
    SUM(total_amount) AS total_spent
FROM orders
GROUP BY customer_id
ORDER BY total_spent DESC;
""")

st.dataframe(customers, use_container_width=True)