import streamlit as st
import pandas as pd
import json

st.title("Converter CSV <-> JSON")

# Selector de tipo de conversión
type_conversion = st.radio("Type of conversion", ("CSV a JSON", "JSON a CSV"))

# Área de carga de archivos
uploaded_file = st.file_uploader("Upload file", type=["csv", "json"])

# Dar nombre del archivo a Descargar
name_file = st.text_input("Enter the name of file to convert")

if uploaded_file is not None:
    # Procesar el archivo según el tipo de conversión
    if type_conversion == "CSV a JSON":
        df = pd.read_csv(uploaded_file)
        json_data = df.to_json(orient="records")
        st.download_button("Descargar JSON", json_data, f"{name_file}.json", "application/json")
    else:
        try:
            json_data = json.load(uploaded_file)
            df = pd.DataFrame(json_data)
            csv_data = df.to_csv(index=False)
            st.download_button("Descargar CSV", csv_data, f"{name_file}.csv", "text/csv")
        except json.JSONDecodeError:
            st.error("Error: File JSON invalid.")
else:
    st.info("Please upload a file to get started.")
