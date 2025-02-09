import streamlit as st
import pandas as pd

data = {
  "Name": ["Christopher"],
  "Age": [20],
  "Student": [True]
}

st.title("Panel of Data Science")
st.write({"Key": "Value"})
state = st.button("Press me")
if state == True:
  st.write(state)

df = pd.DataFrame(data)
df
