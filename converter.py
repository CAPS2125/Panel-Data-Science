import streamlit as st
import pandas as pd

data = {
  "name": ["Christopher"],
  "Age": [20]
}

st.title("Panel of Data Science")
st.write("Update")

df = pd.DataFrame(data)
df
