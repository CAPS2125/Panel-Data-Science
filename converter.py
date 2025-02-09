import streamlit as st
import pandas as pd

data = "https://www.kaggle.com/datasets/hosammhmdali/supermarket-sales"

st.title("Panel of Data Science")
st.write("Update")

df = pd.read_csv(data)
df
