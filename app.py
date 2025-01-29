import streamlit as st
import joblib

# Load the trained model
model = joblib.load('diabetes_model.pkl')

# Streamlit app title
st.title("Diabetes Risk Prediction App")

# Introduction text
st.write("""
This app predicts the risk of diabetes based on user-provided health data. 
Enter the required information below to get a prediction.
""")

# User inputs
age = st.number_input("Age (years)", min_value=1, max_value=120, value=30, step=1)
bmi = st.number_input("Body Mass Index (BMI)", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
glucose = st.number_input("Blood Glucose Level (mg/dL)", min_value=50.0, max_value=300.0, value=120.0, step=1.0)
hba1c = st.number_input("HbA1c Level (%)", min_value=3.0, max_value=15.0, value=5.5, step=0.1)
hypertension = st.selectbox("Do you have hypertension?", ["No", "Yes"])
heart_disease = st.selectbox("Do you have heart disease?", ["No", "Yes"])
gender = st.selectbox("Gender", ["Male", "Female"])
smoking = st.selectbox("Smoking History", ["Never", "Current", "Former", "Ever"])

# Encode inputs
hypertension = 1 if hypertension == "Yes" else 0
heart_disease = 1 if heart_disease == "Yes" else 0
gender = 1 if gender == "Male" else 0
smoking_history = {"Never": 0, "Current": 1, "Former": 2, "Ever": 3}[smoking]

# Prepare input data for prediction
input_data = [[age, bmi, glucose, hba1c, hypertension, heart_disease, gender, smoking_history]]

# Predict diabetes risk
if st.button("Predict"):
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]  # Probability of diabetes (class 1)

    # Display results
    if prediction[0] == 1:
        st.error(f"Prediction: High Risk of Diabetes (Probability: {probability:.2%})")
    else:
        st.success(f"Prediction: Low Risk of Diabetes (Probability: {probability:.2%})")

    st.write("""
    ### Key Factors Influencing Risk
    - High BMI, blood glucose, and HbA1c levels are significant indicators.
    - Lifestyle factors like smoking history and hypertension may contribute to higher risk.
    """)

# Footer
st.write("""
---
This app is for educational purposes and should not replace professional medical advice.
""")
