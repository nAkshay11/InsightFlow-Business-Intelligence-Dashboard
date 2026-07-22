import streamlit as st
from database import run_query

st.set_page_config(
    page_title="Reports",
    page_icon="📑",
    layout="wide"
)

st.title("📑 Business Reports")
st.markdown("### Order Report")
st.divider()

orders = run_query("""
SELECT
    order_id,
    customer_id,
    employee_id,
    order_date,
    order_status,
    payment_status,
    total_amount
FROM orders
ORDER BY order_date DESC;
""")

search = st.text_input("🔍 Search Order ID")

if search:
    orders = orders[
        orders["order_id"].astype(str).str.contains(search)
    ]

st.dataframe(
    orders,
    use_container_width=True,
    hide_index=True
)

csv = orders.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download CSV Report",
    csv,
    "Orders_Report.csv",
    "text/csv"
)