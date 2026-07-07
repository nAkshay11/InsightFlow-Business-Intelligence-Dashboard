import streamlit as st
from database import run_query

st.set_page_config(
    page_title="SQL Studio",
    page_icon="🗄️",
    layout="wide"
)

st.title("🗄️ SQL Studio")
st.markdown("### Execute SQL Queries")
st.divider()

query = st.text_area(
    "Enter SQL Query",
    height=150,
    value="SELECT * FROM orders LIMIT 5;"
)

if st.button("▶ Run Query"):

    try:
        result = run_query(query)
        st.success("Query Executed Successfully")
        st.dataframe(
            result,
            use_container_width=True,
            hide_index=True
        )

    except Exception as e:
        st.error(e)