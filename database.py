import pandas as pd
from sqlalchemy import create_engine
import streamlit as st

@st.cache_resource
def get_engine():
    db_url = st.secrets["DATABASE_URL"]
    return create_engine(db_url)

def run_query(query):
    engine = get_engine()
    return pd.read_sql(query, engine)
