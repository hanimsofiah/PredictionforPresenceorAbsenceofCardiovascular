import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
import os
import joblib
import streamlit as st

def prediction(data):
    data = pd.DataFrame(data).T
    loaded_scaler = joblib.load('min_max_scaler.pkl')
    data=loaded_scaler.transform(data)
    y_probs = new_model.predict(data)
    y_preds = tf.argmax(y_probs,axis=1)
    if y_preds.numpy()[0] == 0:
        return "Elevated"
    elif y_preds.numpy()[0] == 1:
        return "Hypertension 1"
    elif y_preds.numpy()[0] == 2:
        return "Hypertension 2"
    else:
        return "Normal"    

st.title("Cardio Diease Prediction")
st.markdown("Model to predict patient do have cardio disease based on their input")
new_model = tf.keras.models.load_model('cardio_model')
new_model.summary()
st.header("Patient Matrix")
col1,col2 = st.columns(2)
with col1: 
    st.text("Patient Details 1")
    age_in_years = st.number_input("Insert Age in Years")
    height = st.number_input("Insert Height")
    weight = st.number_input("Insert Weight")
    ap_hi = st.number_input("Insert Systolic blood pressure (ap_hi)")
    ap_lo = st.number_input("Insert Diastolic blood pressure (ap_lo)")
    bmi = st.number_input("Insert Body Mass Index (BMI)")
with col2:
    st.text("Patient Details 2")
    gender = st.slider("Gender of the patient. Categorical variable (1: Female, 2: Male).",1,2,0)
    cholesterol = st.slider("Cholesterol levels. Categorical variable (1: Normal, 2: Above Normal, 3: Well Above Normal).",1,3,1)
    gluc = st.slider("Glucose levels. Categorical variable (1: Normal, 2: Above Normal, 3: Well Above Normal).",1,3,1)
    smoke = st.slider("Smoking status. Binary variable (0: Non-smoker, 1: Smoker).",0,1,0)
    alco = st.slider("Alcohol intake. Binary variable (0: Does not consume alcohol, 1: Consumes alcohol).",0,1,0)
    active = st.slider("Physical activity. Binary variable (0: Not physically active, 1: Physically active).",0,1,0)
    cardio = st.slider("Presence or absence of cardiovascular disease. Target variable. Binary (0: Absence, 1: Presence).",0,1,0)

age_in_days = age_in_years * 365
data = [age_in_days,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active,cardio,age_in_years,bmi]

if st.button("Predict Cardio Disease"):
    result = prediction(data)
    st.text(result)
    

