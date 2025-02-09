import streamlit as st

st.title("Converter CSV <-> JSON")

with st.form(key="Input_Data"):
  format = st.selectbox("Select the format", ["CSV", "JSON"])
  st.form_submit_button()
