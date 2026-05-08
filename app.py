import streamlit as st
import pickle
import numpy as np

# Load your trained model
model = pickle.load(open('diabetes_model.sav', 'rb'))

st.title('Diabetes Prediction Web App')

# Create input fields for the user
col1, col2 = st.columns(2)
with col1:
    pregnancies = st.number_input('Number of Pregnancies', min_value=0)
    glucose = st.number_input('Glucose Level', min_value=0)
    blood_pressure = st.number_input('Blood Pressure value', min_value=0)
    skin_thickness = st.number_input('Skin Thickness value', min_value=0)

with col2:
    insulin = st.number_input('Insulin Level', min_value=0)
    bmi = st.number_input('BMI value', format="%.1f")
    dpf = st.number_input('Diabetes Pedigree Function value', format="%.3f")
    age = st.number_input('Age of the Person', min_value=0)

if st.button('Test Result'):
    input_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]
    prediction = model.predict([input_data])
    
    if prediction[0] == 1:
        st.error('The person is likely to have diabetes.')
    else:
        st.success('The person is not likely to have diabetes.')
