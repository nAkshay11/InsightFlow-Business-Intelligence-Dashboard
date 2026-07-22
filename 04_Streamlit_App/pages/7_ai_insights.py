import streamlit as st
from database import run_query

st.set_page_config(
    page_title="AI Insights",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Business Insights")
st.markdown("### AI Generated Business Summary")
st.divider()

# -----------------------------
# Revenue
# -----------------------------
revenue = run_query("""
SELECT SUM(total_amount) AS revenue
FROM orders;
""")

total_revenue = revenue.iloc[0]["revenue"]

# -----------------------------
# Orders
# -----------------------------
orders = run_query("""
SELECT COUNT(*) AS total_orders
FROM orders;
""")

total_orders = orders.iloc[0]["total_orders"]

# -----------------------------
# Customers
# -----------------------------
customers = run_query("""
SELECT COUNT(*) AS total_customers
FROM customers;
""")

total_customers = customers.iloc[0]["total_customers"]

# -----------------------------
# Highest Order
# -----------------------------
highest = run_query("""
SELECT
order_id,
customer_id,
total_amount
FROM orders
ORDER BY total_amount DESC
LIMIT 1;
""")

st.success(f"💰 Total Revenue : ₹{total_revenue:,.0f}")

st.info(f"📦 Total Orders : {total_orders}")

st.info(f"👥 Total Customers : {total_customers}")

st.warning(
    f"🏆 Highest Order : Order #{highest.iloc[0]['order_id']} "
    f"(Customer {highest.iloc[0]['customer_id']}) "
    f"₹{highest.iloc[0]['total_amount']:,.0f}"
)

st.divider()

st.subheader("💡 AI Recommendations")

st.write("✅ Revenue is growing steadily.")

st.write("✅ Focus on high-value customers.")

st.write("✅ Improve Processing orders to increase delivery speed.")

st.write("✅ Monitor cancelled orders to reduce revenue loss.")

st.write("✅ Increase marketing during high-performing months.")