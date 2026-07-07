from database import run_query
import streamlit as st

def login(email, password):

    query = f"""
    SELECT *
    FROM users
    WHERE email='{email}'
    AND password_hash='{password}'
    AND status='Active'
    """

    user = run_query(query)

    if len(user) > 0:
        st.session_state["logged_in"] = True
        st.session_state["user_name"] = user.iloc[0]["full_name"]
        st.session_state["email"] = user.iloc[0]["email"]
        st.session_state["role_id"] = user.iloc[0]["role_id"]
        return True

    return False