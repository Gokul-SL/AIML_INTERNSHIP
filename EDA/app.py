import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")


st.title("Student Pass Prediction")

st.write("Enter the number of study hours.")

hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    step=0.5
)


if st.button("Predict"):

   
    prediction = model.predict([[hours]])

    
    if prediction[0] == 1:
        st.success("Student will PASS")
    else:
        st.error("Student will FAIL")