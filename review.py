
import streamlit as st
st.title("Fake review detection")
import numpy as np
import joblib
model = joblib.load('review_kaggle_model.pkl')


user_input = st.text_input(" Enter review :")

if st.button("Predict"):
    prediction = model.predict([user_input])[0]
    if prediction == 'OR':
        st.success(" Real review")

    else:
        st.error(" Fake review ")    