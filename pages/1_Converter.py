import streamlit as st

st.title("Converter CSV <-> JSON")

with st.form(key="Input_Data"):
  format_to = st.radio("Select the format Origin", ["CSV to JSON", "JSON to CSV"])
  if format_to == "CSV to JSON":
    orient_json = st.selectbox("Select the order of JSON", ["table", "records", "index", "split", "columns", "values"])
  uploaded_file = st.file_uploader("Upload a file", type=["csv", "json"])
  st.form_submit_button()
