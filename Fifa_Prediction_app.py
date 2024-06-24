import streamlit as st
import pandas as pd
import pickle

# Load the scalers and model
with open('Fifa_Regression_Model.pkl', 'rb') as file:
        model = pickle.load(file)

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
    print(input_df)
    # Make prediction
    prediction = model.predict(input_df)
    
    # Display prediction and confidence interval
    st.write(f"Predicted Overall Rating: {prediction[0]:.2f}")

