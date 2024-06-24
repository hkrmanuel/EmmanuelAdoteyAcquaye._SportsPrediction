import streamlit as st
import pandas as pd
import pickle

# Load the model
try:
    with open('Fifa_Regression_Model.pkl', 'rb') as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"Error loading model: {e}")

st.title("FIFA Player Rating Predictor")

# Input variables
input_var = ['movement_reactions', 'potential', 'passing', 'wage_eur', 'value_eur', 'dribbling']
inputs = {}

# Collect input data from the user
for feature in input_var:
    inputs[feature] = st.number_input(f"Enter {feature}", value=0.0)

# Predict button
if st.button("Predict"):
    input_df = pd.DataFrame([inputs])
    st.write(input_df)
    # Make prediction
    try:
        prediction = model.predict(input_df)
        st.write(f"Predicted Overall Rating: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")


