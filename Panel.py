import streamlit as st
import pandas as pd

st.title("Panel")

tab1, tab2 = st.tabs(["Step 1", "Step 2"])

with tab1:
  st.header("Step 1. Upload File to Work")
  with st.form(key="Upload_data"):
    upload_file = st.file_uploader("Form of file", type=["csv"])
    file_data = st.form_submit_button("Download data")

with tab2:
  st.header("Step 2. View the dataset")
  if file_data == True:
    data = pd.read_csv(upload_file)
    st.data_editor(data)