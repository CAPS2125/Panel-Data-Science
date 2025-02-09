import streamlit as st
import pandas as pd
import json

st.title("CSV <-> JSON Converter")

# Formulario
with st.form("converter_form"):  # Encapsula todo en un formulario
    name_file = st.text_input("Enter the file name to download (without extension)")
    type_conversion = st.radio("Conversion Type", ("CSV to JSON", "JSON to CSV"))
    uploaded_file = st.file_uploader("Upload File", type=["csv", "json"])
    submitted = st.form_submit_button("Convert") # Botón de envío del formulario

if submitted: # Solo procesa si se envió el formulario
    if uploaded_file is not None:
        if name_file == "": # Validación del nombre del archivo
            st.error("Please enter a file name.")
        else:
            try:
                if type_conversion == "CSV to JSON":
                    df = pd.read_csv(uploaded_file)
                    json_data = df.to_json(orient="records", indent=4) # Indentación para mejor legibilidad
                    st.download_button("Download JSON", json_data, f"{name_file}.json", "application/json")
                else:  # JSON to CSV
                    try:
                        json_data = json.load(uploaded_file)
                        df = pd.DataFrame(json_data)
                        csv_data = df.to_csv(index=False)
                        st.download_button("Download CSV", csv_data, f"{name_file}.csv", "text/csv")
                    except json.JSONDecodeError:
                        st.error("Error: Invalid JSON file.")
            except pd.errors.EmptyDataError: # Manejo de archivos CSV vacíos
                st.error("Error: Empty CSV file.")

    else:
        st.error("Please upload a file.")
