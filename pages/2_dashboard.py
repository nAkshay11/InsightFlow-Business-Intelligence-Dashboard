import pandas as pd
import plotly.express as px
import streamlit as st
from database import run_query
from datetime import datetime

st.set_page_config(
    page_title="InsightFlow Dashboard",
    page_icon="📊",
    layout="wide"
)
with open("styles/style.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )

# ==========================================
# EXPORT FUNCTION
# ==========================================
def export_orders(df):
    df.to_excel(
        "Latest_Orders_Report.xlsx",
        index=False
    )

# ==========================================
# USER SESSION
# ==========================================
if "user_name" not in st.session_state:
    st.warning("Please login first.")
    st.switch_page("pages/1_login.py")

role_names = {
    1: "Administrator",
    2: "Analyst",
    3: "Data Engineer",
    4: "Business Manager"
}

user_name = st.session_state.get("user_name", "User")
role = role_names.get(
    st.session_state.get("role_id", 0),
    "User"
)

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:

   st.markdown("""
<div style="
background:#37475A;
padding:20px;
border-radius:12px;
text-align:center;
margin-bottom:15px;
">

<h2 style="color:white;margin:0;">
📊 InsightFlow
</h2>

<p style="color:#D1D5DB;margin-top:8px;">
Enterprise BI Platform
</p>

</div>
""", unsafe_allow_html=True)

st.success("🟢 Database Connected")
st.info(f"👤 User: {user_name}")
st.warning(f"🎭 Role: {role}")

st.divider()

status = st.selectbox(
    "Order Status",
    [
        "All",
        "Delivered",
        "Shipped",
        "Processing",
        "Cancelled"
    ]
)

customer = st.selectbox(
        "Customer",
        [
            "All",
            "Customer 1",
            "Customer 2",
            "Customer 3"
        ]
    )

if st.button("Apply Filters", use_container_width=True):
            st.toast("Filters Applied")

st.markdown("---")

if st.button("🚪 Logout", use_container_width=True):
            st.session_state.clear()
            st.switch_page("pages/1_login.py")

# ==========================================
# FILTER
# ==========================================
filter_query = ""

if status != "All":
    filter_query = f"""
    WHERE order_status='{status}'
    """

# ==========================================
# HEADER
# ==========================================
st.markdown(f"""
<div style="
background:linear-gradient(90deg,#232F3E,#37475A);
padding:30px;
border-radius:18px;
color:white;
margin-bottom:25px;
box-shadow:0px 8px 20px rgba(0,0,0,.25);
">

<h1>📊 InsightFlow</h1>

<h3>Enterprise Business Intelligence Platform</h3>

<hr style="border:1px solid rgba(255,255,255,.2);">

<h3>👋 Welcome back, {user_name}</h3>

<p>🎭 {role}</p>

</div>
""", unsafe_allow_html=True)

st.success("🟢 System Status : Online")
st.info(f"👤 Logged User : {user_name}")
st.warning(f"🎭 Role : {role}")
st.divider()

st.info(
    f"📅 Today | 👤 {user_name} | 🎭 {role}"
)
st.caption(
    f"🕒 Last Updated: {datetime.now().strftime('%d %b %Y, %I:%M %p')}"
)

st.divider()

# ==========================================
# KPI DATA
# ==========================================
revenue = run_query("""
SELECT
SUM(total_amount) revenue
FROM orders;
""")

orders = run_query("""
SELECT
COUNT(*) total_orders
FROM orders;
""")

customers = run_query("""
SELECT
COUNT(*) total_customers
FROM customers;
""")

total_revenue = revenue.iloc[0]["revenue"]
total_orders = orders.iloc[0]["total_orders"]
total_customers = customers.iloc[0]["total_customers"]

profit = total_revenue * 0.20

# ==========================================
# KPI CARDS
# ==========================================
st.subheader("📈 Business Overview")
st.caption("Real-time KPIs and business performance")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="💰 Revenue",
        value=f"₹{total_revenue:,.0f}",
        delta="+12%"
    )

with col2:
    st.metric(
        label="📦 Orders",
        value=total_orders,
        delta="+8%"
    )

with col3:
    st.metric(
        label="👥 Customers",
        value=total_customers,
        delta="+15%"
    )

with col4:
    st.metric(
        label="📈 Profit",
        value=f"₹{profit:,.0f}",
        delta="+10%"
    )

st.divider()

# ==========================================
# SALES & MONTHLY REVENUE
# ==========================================

st.markdown("## 📊 Sales Analytics")
st.caption("Revenue trends and monthly business growth")

left, right = st.columns([1, 1], gap="large")

with left:

    st.subheader("📈 Sales Trend")

    sales = run_query(f"""
    SELECT
        order_date,
        total_amount
    FROM orders
    {filter_query}
    ORDER BY order_date;
    """)

    fig = px.line(
        sales,
        x="order_date",
        y="total_amount",
        markers=True,
        template="plotly_white"
    )

    fig.update_layout(
        margin=dict(l=20,r=20,t=30,b=20),
        height=400
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.write("")

with right:

    st.subheader("📊 Monthly Revenue")

    monthly = run_query("""
SELECT
    DATE_TRUNC('month', order_date) AS month_date,
    SUM(total_amount) AS revenue
FROM orders
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY DATE_TRUNC('month', order_date);
""")

    fig = px.bar(
        monthly,
        x="month_date",
        y="revenue",
        text="revenue",
        template="plotly_white",
        color="revenue"
    )

    fig.update_layout(
        margin=dict(l=20,r=20,t=30,b=20),
        height=400,
        coloraxis_showscale=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.write("")
st.divider()

# ==========================================
# PIE & TOP CUSTOMERS
# ==========================================

# ==========================================
# ORDER STATUS & TOP CUSTOMERS
# ==========================================

st.markdown("## 👥 Customer Insights")
st.caption("Customer behaviour and order distribution")

left, right = st.columns([1,1], gap="large")

with left:

    st.subheader("🥧 Order Status")

    status_data = run_query("""
    SELECT
        order_status,
        COUNT(*) total_orders
    FROM orders
    GROUP BY order_status
    ORDER BY total_orders DESC;
    """)

    fig = px.pie(
        status_data,
        names="order_status",
        values="total_orders",
        hole=.55
    )

    fig.update_layout(
        height=400
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.write("")

with right:

    st.subheader("👥 Top Customers")

    top_customers = run_query("""
    SELECT
        customer_id,
        COUNT(order_id) total_orders,
        SUM(total_amount) total_spent
    FROM orders
    GROUP BY customer_id
    ORDER BY total_spent DESC;
    """)

    st.dataframe(
        top_customers,
        use_container_width=True,
        hide_index=True
    )

st.divider()

# ==========================================
# LATEST ORDERS
# ==========================================

st.markdown("## 📋 Latest Orders")
st.caption("Most recent customer orders")

latest_orders = run_query(f"""
SELECT
    order_id,
    customer_id,
    order_date,
    total_amount,
    order_status
FROM orders
{filter_query}
ORDER BY order_date DESC
LIMIT 10;
""")

st.dataframe(
    latest_orders,
    use_container_width=True,
    hide_index=True,
    height=350
)

st.write("")

# ==========================================
# EXPORT
# ==========================================

left, right = st.columns([8,2])

with right:

    if st.button(
    "📥 Download Excel Report",
    use_container_width=True
):
        export_orders(latest_orders)
        st.success("Excel exported successfully!")

st.divider()

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.markdown("""
<div style="text-align:center; padding:20px; color:gray;">

<b>📊 InsightFlow Enterprise BI Platform</b><br><br>

Powered by Python • Streamlit • PostgreSQL • Plotly • Pandas

<br><br>

Version 1.0.0

<br>

© 2026 Akshay Chandra

</div>
""", unsafe_allow_html=True)