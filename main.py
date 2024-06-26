import streamlit as st

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
    # Prepare the data for prediction
    data = {
        "age": age,
        "gender": gender,
        "total_bilirubin": total_bilirubin,
        "direct_bilirubin": direct_bilirubin,
        "alkaline_phosphotase": alkaline_phosphotase,
        "alamine_aminotransferase": alamine_aminotransferase,
        "aspartate_aminotransferase": aspartate_aminotransferase,
        "total_proteins": total_proteins,
        "albumin": albumin,
        "albumin_and_globulin_ratio": albumin_and_globulin_ratio
    }
    
    # Parse the response
    result = ()
    prediction = result.get("prediction", 0)
    prediction_text = "Positive for Liver Disease" if prediction == 1 else "Negative for Liver Disease"
    
    # Display the prediction result
    st.header("Prediction Result")
    st.subheader(prediction_text)
