import streamlit as st
with open("styles/style.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )


st.set_page_config(
    page_title="InsightFlow",
    page_icon="📊",
    layout="wide"
)
hide_streamlit = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit, unsafe_allow_html=True)

st.title("📊 InsightFlow")
st.subheader("Enterprise Business Intelligence Platform")

st.success("Application Started Successfully 🚀")

st.info("👈 Select **Login** from the left sidebar to continue.")