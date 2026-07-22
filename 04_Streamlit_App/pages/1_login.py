import streamlit as st
with open("styles/style.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )
from auth import login

st.set_page_config(
    page_title="InsightFlow Login",
    page_icon="🔐",
    layout="centered"
)

st.markdown(
    """
    <style>
    .login-box{
        padding:30px;
        border-radius:15px;
        background-color:white;
        box-shadow:0px 4px 15px rgba(0,0,0,0.15);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='login-box'>", unsafe_allow_html=True)

st.markdown(
    "<h1 style='text-align:center;'>📊 InsightFlow</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align:center;color:gray;'>Enterprise Business Intelligence Platform</h4>",
    unsafe_allow_html=True
)

st.write("")

email = st.text_input(
    "📧 Email Address",
    placeholder="Enter your email"
)

password = st.text_input(
    "🔒 Password",
    type="password",
    placeholder="Enter your password"
)
remember = st.checkbox("Remember Me")

if st.button("🚀 Sign In", use_container_width=True):

    if login(email, password):
        st.success("✅ Login Successful! Redirecting to Dashboard...")
        st.switch_page("pages/2_dashboard.py")
    else:
        st.error("❌ Invalid email or password. Please try again.")

st.write("")
st.info("🔐 Secure Login • PostgreSQL Authentication • Enterprise Access")
st.markdown(
    "<p style='text-align:center;color:gray;'>Forgot Password?</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<hr><p style='text-align:center;color:gray;'>© 2026 InsightFlow | Version 1.0</p>",
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)