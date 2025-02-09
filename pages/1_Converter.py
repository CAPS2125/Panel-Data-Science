import streamlit as st
import pandas as pd
import json

st.title("Conversor CSV <-> JSON")

# Selector de tipo de conversión
tipo_conversion = st.radio("Tipo de conversión", ("CSV a JSON", "JSON a CSV"))

# Área de carga de archivos
archivo_cargado = st.file_uploader("Cargar archivo", type=["csv", "json"])

if archivo_cargado is not None:
    # Procesar el archivo según el tipo de conversión
    if tipo_conversion == "CSV a JSON":
        df = pd.read_csv(archivo_cargado)
        json_data = df.to_json(orient="records")
        st.download_button("Descargar JSON", json_data, "datos.json", "application/json")
    else:
        try:
            json_data = json.load(archivo_cargado)
            df = pd.DataFrame(json_data)
            csv_data = df.to_csv(index=False)
            st.download_button("Descargar CSV", csv_data, "datos.csv", "text/csv")
        except json.JSONDecodeError:
            st.error("Error: Archivo JSON inválido.")
else:
    st.info("Por favor, carga un archivo para comenzar.")
