import streamlit as st

st.title("Converter CSV <-> JSON")

with st.form(key="Input_Data"):
  format = st.selectbox("Select the format", ["CSV", "JSON"])
  uploaded_file = st.file_uploader("Upload a file", type=["csv", "json"])
  st.form_submit_button()
