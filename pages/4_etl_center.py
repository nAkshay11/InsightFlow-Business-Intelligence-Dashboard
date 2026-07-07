import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ETL Center",
    page_icon="🔄",
    layout="wide"
)

st.title("🔄 ETL Center")
st.markdown("### Upload and Process Data")
st.divider()

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("File Uploaded Successfully!")

    st.subheader("Preview")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("Dataset Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", len(df))

    with col2:
        st.metric("Columns", len(df.columns))

    with col3:
        st.metric("Missing Values", df.isnull().sum().sum())

    st.divider()

    if st.button("Remove Duplicates"):
        df = df.drop_duplicates()
        st.success("Duplicates Removed Successfully!")

    if st.button("Remove Missing Values"):
        df = df.dropna()
        st.success("Missing Values Removed Successfully!")

    st.divider()

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )