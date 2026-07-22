from database import run_query

df = run_query("SELECT COUNT(*) AS total_customers FROM customers;")

print(df)