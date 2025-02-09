import streamlit as st
import pandas as pd

st.title("Panel")
upload_file = st.file_uploader("Upload File", type=["csv", "json"])
if upload_file is not None:
  data = pd.read_csv(upload_file)
  st.data_editor(data)