import streamlit as st

st.title("Streamlit  by Atharva Deshmukh")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome {name}")