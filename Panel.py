import streamlit as st
import pandas as pd

st.set_page_config(page_title="Main Panel")
st.title("Panel")

data = None
tab1, tab2, tab3 = st.tabs(["Step 1", "Step 2", "Step 3"])

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

with tab3:
  st.header("Step 3. Dataset information")
  if data is not None:
    col1, col2, col3 = st.columns(3)
    with col1:
      dtypes_df = data.dtypes.to_frame(name='dtypes')
      st.metric(label="Rows", value=data.shape[0])
      st.write("Data types")
      st.dataframe(dtypes_df)
    with col2:
      data_unique_counts = data.nunique().to_frame(name='count')
      st.metric(label="Columns", value=data.shape[1])
      st.write("Number of unique values")
      st.dataframe(data_unique_counts)

    with col3:
      amount_data = data.shape[0] * data.shape[1]
      null_check = pd.DataFrame(data.isnull().any(), columns=['Nulls'])
      st.metric(label="Amount of data", value=amount_data)
      st.write("Does it have null values?")
      st.dataframe(null_check)
      