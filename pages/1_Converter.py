import streamlit as st

st.title("Converter CSV <-> JSON")

option_orient = st.checkbox("Change orient of JSON")

with st.form(key="Input_Data"):
  format_to = st.radio("Select the format Origin", ["CSV to JSON", "JSON to CSV"])
  if option_orient:
      orient_json = st.selectbox("Select the order of JSON", ["table", "records", "index", "split", "columns", "values"])
  uploaded_file = st.file_uploader("Upload a file", type=["csv", "json"])
  st.form_submit_button()
