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
    if feature in ['value_eur', 'wage_eur']:
        inputs[feature] = st.number_input(f"Enter {feature}", value=0.0, step=1000.0)
    else:
        inputs[feature] = st.number_input(f"Enter {feature}", value=0.0, step=1.0, min_value=0.0, max_value=100.0)
    
    if inputs[feature] < 0:
        st.error(f"Please enter a non-negative value for {feature}")
        
# Predict button
if st.button("Predict"):
    input_df = pd.DataFrame([inputs])
    # Make prediction
    try:
        prediction = model.predict(input_df)
        st.write(f"Predicted Overall Rating: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")


