import streamlit as st
import pandas as pd

data = {
  "Name": ["Christopher"],
  "Age": [20],
  "Student": [True]
}

# JSON Example with write
st.write({"Key": "Value"})

#Button Demo
state = st.button("Press me")
if state == True:
  st.write(state)

# Text Elements
st.title("Title: Panel of Data Science")
st.header("Header: Testing")
st.subheader("Subheader: Testing the framework Streamlit")
st.markdown("This is _Markdown_")
st.caption("Small Text")
code_example = """
def add(a, b):
  return a + b
"""
st.code(code_example, language="python")
st.divider()

# DataFrames
st.subheader("Dataframe")
df = {
  "Name": ["Christopher", "Julian", "Lira"],
  "Age": [20, 19, 20],
  "Carrer": ["Data Science", "Computer Science", "Enginner ..."]
}
st.dataframe(df)
