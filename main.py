import streamlit as st
import numpy as np
from sklearn.linear_model import LogisticRegression

# Dummy model for demonstration
# In practice, you would load a pre-trained model, for example using joblib
model = LogisticRegression()

# Dummy data to train the model
# In practice, use your real training data
X_train = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0.5],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1.0],
                    [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1.5],
                    [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 2.0]])

y_train = np.array([0, 1, 0, 1])  # Dummy target values

model.fit(X_train, y_train)

# Set up the page layout and title
st.set_page_config(layout="wide")
st.title("Liver Disease Prediction App")

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
        
        # Make prediction
        prediction = model.predict(inputs)[0]
        prediction_text = "Positive for Liver Disease" if prediction == 1 else "Negative for Liver Disease"
        
    except ValueError as e:
        prediction_text = f"Invalid input: {e}"
    except Exception as e:
        prediction_text = f"An error occurred: {e}"
    
    # Display the prediction result
    st.header("Prediction Result")
    st.subheader(prediction_text)
