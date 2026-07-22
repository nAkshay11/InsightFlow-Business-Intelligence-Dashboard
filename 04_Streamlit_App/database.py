import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:@localhost:5432/InsightFlow"
)

def run_query(query):
    return pd.read_sql(query, engine)