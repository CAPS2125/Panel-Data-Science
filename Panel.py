import streamlit as st
import pandas as pd

class filter_dataset:
    def filter(self, df, column, operator, value):
        match operator:
            case "Equal":
                new_df = df[df[column] == value]
            case "Unequal":
                new_df = df[df[column] != value]
            case "less than":
                new_df = df[df[column] < value]
            case "greater than":
                new_df = df[df[column] > value]
            case "Lesser equal":
                new_df = df[df[column] <= value]
            case "greater equal":
                new_df = df[df[column] >= value]
        return new_df

ins_filter = filter_dataset()

st.set_page_config(page_title="Main Panel")
st.title("Panel")

if "data" not in st.session_state:
  st.session_state.data = None
operators = ["Equal", "Unequal", "less than", "greater than", "Lesser equal", "greater equal"]
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Step 1", "Step 2", "Step 3", "Step 4", "Step 5"])

with tab1:
  st.header("Step 1. Upload File to Work")
  with st.form(key="Upload_data"):
    upload_file = st.file_uploader("Form of file", type=["csv"])
    file_data = st.form_submit_button("Download data")

with tab2:
  st.header("Step 2. View the dataset")
  if file_data or st.session_state.data is not None:
    st.session_state.data = pd.read_csv(upload_file)
    st.data_editor(st.session_state.data)

with tab3:
  st.header("Step 3. Dataset information")
  if st.session_state.data is not None:
    col1, col2, col3 = st.columns(3)
    with col1:
      dtypes_df = st.session_state.data.dtypes.to_frame(name='dtypes')
      st.metric(label="Rows", value=st.session_state.data.shape[0])
      st.write("Data types")
      st.dataframe(dtypes_df)
    with col2:
      data_unique_counts = st.session_state.data.nunique().to_frame(name='count')
      st.metric(label="Columns", value=st.session_state.data.shape[1])
      st.write("Number of unique values")
      st.dataframe(data_unique_counts)

    with col3:
      amount_data = st.session_state.data.shape[0] * st.session_state.data.shape[1]
      null_check = pd.DataFrame(st.session_state.data.isnull().any(), columns=['Nulls'])
      st.metric(label="Amount of data", value=amount_data)
      st.write("Does it have null values?")
      st.dataframe(null_check)
with tab4:
  st.header("Step 4. Data transformation")
  if st.session_state.data is not None:
    st.subheader("Create column from a condition")
    with st.form(key="Apply"):
      column_apply = st.selectbox("Select column that will be taken as a parameter",
                            list(st.session_state.data.columns))
      st.form_submit_button()
with tab5:
  st.header("Step 5. Filter Data")
  if st.session_state.data is not None:
    with st.form(key="Filter"):
      column_filter = st.selectbox("Select column that will be taken as a parameter",
                            list(st.session_state.data.columns))
      logical_operator = st.selectbox("Select the type of operation", operators)
      value = st.text_input("Value to compare (From the column data type)")
      filtered_dataset = st.form_submit_button(label="Filter")
    if filtered_dataset:
      if value == None:
        st.warning("Please fill in all of the fields")
      else:
        new_df = ins_filter.filter(st.session_state.data, column_filter, logical_operator, value)
        st.dataframe(new_df)