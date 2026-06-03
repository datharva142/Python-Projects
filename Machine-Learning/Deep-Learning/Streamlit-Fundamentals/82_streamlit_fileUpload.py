import streamlit as st

st.title("Streamlit  by Atharva Deshmukh")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:
    st.success("PDF Uploaded Successfully")