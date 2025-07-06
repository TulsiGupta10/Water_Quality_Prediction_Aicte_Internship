import pandas as pd
import numpy as np
import joblib
import streamlit as st

# Load model and model columns
model = joblib.load("pollution_model.pkl")
model_cols = joblib.load("model_columns.pkl")

# UI
st.title("💧 Water Pollutants Predictor")
st.write("Predict the water pollutants based on Year and Station ID")

# User Inputs
year_input = st.number_input("Enter Year", min_value=2000, max_value=2100, value=2022)
station_id = st.text_input("Enter Station ID", value='1')

# Predict Button
if st.button("Predict"):
    if not station_id:
        st.warning("Please enter a valid Station ID.")
    else:
        # Build input DataFrame
        input_df = pd.DataFrame({'year': [year_input], 'id': [station_id]})
        input_encoded = pd.get_dummies(input_df, columns=['id'])

        # Add any missing columns from training
        for col in model_cols:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        input_encoded = input_encoded[model_cols]  # align column order

        try:
            prediction = model.predict(input_encoded)
            predicted_pollutants = prediction[0]

            # If prediction is a list/array of pollutant levels
            pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']
            st.subheader(f"Predicted pollutant levels for station '{station_id}' in {year_input}:")
            for p, val in zip(pollutants, predicted_pollutants):
                st.write(f"**{p}**: {val:.2f}")
        except Exception as e:
            st.error(f"Prediction failed: {e}")
