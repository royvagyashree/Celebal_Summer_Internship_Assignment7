import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("credit_card_model.pkl")

st.set_page_config(page_title="Credit Card Fraud Detection", page_icon="💳")
st.title("💳 Credit Card Fraud Detection App")

st.write("Enter the following transaction details:")

# Feature list used during model training
feature_names = [
    "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10",
    "V11", "V12", "V13", "V14", "V15", "V16", "V17", "V18", "V19", "V20",
    "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28", "Amount"
]

# Dynamically collect input for all features
input_values = []
for feature in feature_names:
    val = st.number_input(f"{feature}", format="%.6f")
    input_values.append(val)

# Predict on click
if st.button("Predict"):
    input_df = pd.DataFrame([input_values], columns=feature_names)
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction Looks Legit.")
