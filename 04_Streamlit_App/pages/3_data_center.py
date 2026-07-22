import streamlit as st
from database import run_query

st.set_page_config(
    page_title="Data Center",
    page_icon="🗂️",
    layout="wide"
)

st.title("🗂️ Data Center")
st.markdown("### Database Overview")
st.divider()

# -----------------------------
# Total Customers
# -----------------------------
customers = run_query("""
SELECT COUNT(*) AS total_customers
FROM customers;
""")

# -----------------------------
# Total Orders
# -----------------------------
orders = run_query("""
SELECT COUNT(*) AS total_orders
FROM orders;
""")

# -----------------------------
# Total Products
# -----------------------------
products = run_query("""
SELECT COUNT(*) AS total_products
FROM products;
""")

# -----------------------------
# Total Employees
# -----------------------------
employees = run_query("""
SELECT COUNT(*) AS total_employees
FROM employees;
""")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Customers", customers.iloc[0]["total_customers"])

with col2:
    st.metric("📦 Orders", orders.iloc[0]["total_orders"])

with col3:
    st.metric("🛒 Products", products.iloc[0]["total_products"])

with col4:
    st.metric("👨‍💼 Employees", employees.iloc[0]["total_employees"])

st.divider()

st.subheader("📋 Database Tables")

tables = run_query("""
SELECT table_name
FROM information_schema.tables
WHERE table_schema='public'
ORDER BY table_name;
""")

st.dataframe(
    tables,
    use_container_width=True,
    hide_index=True
)