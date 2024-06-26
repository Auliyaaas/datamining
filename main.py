import streamlit as st
import numpy as np

st.title("Liver Disease Prediction App")

# Mock prediction function
def mock_predict(inputs):
    # Simple logic to mock the prediction
    # For demonstration purposes only, replace with actual model logic
    if inputs[0][2] > 1.2:  # Arbitrary condition based on Total Bilirubin
        return [1]  # Positive for Liver Disease
    else:
        return [0]  # Negative for Liver Disease

# Create a form for user input
with st.form("prediction_form"):
    st.header("Enter Patient Details")
    
    age = st.text_input("Age")
    gender = st.selectbox("Gender", ["Female", "Male"])
    total_bilirubin = st.text_input("Total Bilirubin (0 - 75, bisa dalam bentuk desimal)")
    direct_bilirubin = st.text_input("Direct Bilirubin (0 - 20, bisa dalam bentuk desimal)")
    alkaline_phosphotase = st.text_input("Alkaline Phosphotase (50 - 2210)")
    alamine_aminotransferase = st.text_input("Alamine Aminotransferase (10 - 2000)")
    aspartate_aminotransferase = st.text_input("Aspartate Aminotransferase (10 - 4930)")
    total_proteins = st.text_input("Total Proteins (2.0 - 9.8)")
    albumin = st.text_input("Albumin (0.8 - 5.8)")
    albumin_and_globulin_ratio = st.text_input("Albumin and Globulin Ratio (0.2 - 3.0)")
    
    # Submit button
    submitted = st.form_submit_button("Predict")

# If the form is submitted, make the prediction
if submitted:
    try:
        # Convert inputs to the right format
        inputs = np.array([
            float(age),
            1 if gender == "Male" else 0,
            float(total_bilirubin),
            float(direct_bilirubin),
            float(alkaline_phosphotase),
            float(alamine_aminotransferase),
            float(aspartate_aminotransferase),
            float(total_proteins),
            float(albumin),
            float(albumin_and_globulin_ratio)
        ]).reshape(1, -1)
        
        # Log inputs for debugging
        st.write("Inputs:", inputs)
        
        # Make prediction using the mock function
        prediction = mock_predict(inputs)[0]
        prediction_text = "Positive for Liver Disease" if prediction == 1 else "Negative for Liver Disease"
        
    
    # Display the prediction result
    st.header("Prediction Result")
    st.subheader(prediction_text)
