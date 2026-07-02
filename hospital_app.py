import streamlit as st
import pandas as pd
import pickle

with open ("hospital_model (1).pkl", "rb") as f:
  bundle = pickle.load(f)
  st.write("Connected")
