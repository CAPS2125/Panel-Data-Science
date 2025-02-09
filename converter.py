import streamlit as st
import pandas as pd

data = {
  "Name": ["Christopher"],
  "Age": [20],
  "Student": [True]
}

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

# JSON Example with write
st.write({"Key": "Value"})
#Button Demo
state = st.button("Press me")
if state == True:
  st.write(state)

df = pd.DataFrame(data)
df
