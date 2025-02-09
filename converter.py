import streamlit as st
import pandas as pd

data = {
  "Name": ["Christopher"],
  "Age": [20],
  "Student": [True]
}

st.title("Panel of Data Science")
st.write({"Key": "Value"})

df = pd.DataFrame(data)
df
