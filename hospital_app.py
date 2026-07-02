import streamlit as st
import pandas as pd
import pickle

with open ("hospital_model (1).pkl", "rb") as f:
  bundle = pickle.load(f)
  st.write("Connected")

model = bundle["model"]
scaler = bundle["scaler"]

features = bundle["features"]
cols_to_scale = bundle["cols_to_scale"]

dept_map_inv = bundle["dept_map_inv"]
gender_map = bundle["gender_map"]
temp_map = bundle["tempt_map"]
hr_map = bundle["hr_map"]
cc_map = bundle["cc_map"]

DEPT_INFO = {
    "Respiratory Medicine": {
        "icon": "🫁",
        "desc": "Specialises in conditions affecting the lungs and airways.",
        "next": [
            "Visit Level 2, Wing B",
            "Estimated wait: 15–25 minutes",
            "Please wear a mask"
        ]
    },

    "Cardiology": {
        "icon": "❤️",
        "desc": "Specialises in heart and cardiovascular conditions.",
        "next": [
            "Visit Level 3, Wing A",
            "Estimated wait: 20–30 minutes",
            "Bring previous ECG reports"
        ]
    },

    "Gastroenterology": {
        "icon": "🫃",
        "desc": "Specialises in digestive system conditions.",
        "next": [
            "Visit Level 1, Wing C",
            "Estimated wait: 10–20 minutes"
        ]
    },

    "Neurology": {
        "icon": "🧠",
        "desc": "Specialises in brain and nervous system conditions.",
        "next": [
            "Visit Level 4, Wing A",
            "Bring current medications list"
        ]
    },

    "General Medicine": {
        "icon": "🩺",
        "desc": "General health consultation.",
        "next": [
            "Visit Level 1, Wing A"
        ]
    },

    "Dermatology": {
        "icon": "🔬",
        "desc": "Specialises in skin conditions.",
        "next": [
            "Visit Level 2, Wing D"
        ]
    }
}

st.title("Smart Hospital Navigator🏥")
st.write("Fill in the patient's information below")

st.header("Patient Information")
age = st.number_input("Age", min_value=1, max_value=120, value=30)
gender = st.selectbox("Gender", ["Female", "Male"])

st.header("Symptoms")

col1, col2 = st.columns(2)

with col1:
  fever = st.checkbox("Fever")
  cough = st.checkbox("Cough")
  headache = st.checkbox("Headache")
  chest_pain = st.checkbox("Chest Pain")
  stomach_pain = st.checkbox("Stomach Pain")
  
  
