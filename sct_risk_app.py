import streamlit as st

# Title
st.title("Sickle Cell Trait (SCT) Risk Assessment")

# Introduction
st.write("""
This tool helps assess risk levels for individuals with **Sickle Cell Trait (SCT)** 
based on factors like hydration, medical history, and physical activity.
""")

# User Inputs
sct = st.radio("Do you have Sickle Cell Trait (SCT)?", ["Yes", "No"])
cramps = st.radio("Have you ever experienced severe muscle cramps or heat exhaustion?", ["Yes", "No"])
medical = st.radio("Have you needed medical attention due to extreme fatigue, cramps, or fainting?", ["Yes", "No"])
hydration = st.radio("Do you hydrate properly before and after exercise?", ["Yes", "No"])

# Risk Calculation Logic
risk_level = "Low Risk"

if sct == "Yes":
    if cramps == "Yes" or medical == "Yes" or hydration == "No":
        risk_level = "Moderate Risk"
    if cramps == "Yes" and medical == "Yes" and hydration == "No":
        risk_level = "High Risk"
elif sct == "No":
    if cramps == "Yes" or medical == "Yes":
        risk_level = "Moderate Risk"

# Display Risk Level
st.subheader("Your Risk Assessment Result:")
st.write(f"**{risk_level}**")

# Recommendations
st.subheader("Precautionary Recommendations:")
if risk_level == "Low Risk":
    st.write("✅ Keep maintaining proper hydration and monitoring your health.")
elif risk_level == "Moderate Risk":
    st.write("⚠️ Consider consulting a healthcare provider and improving hydration before intense activities.")
elif risk_level == "High Risk":
    st.write("🚨 High risk detected! Consult a doctor before engaging in high-intensity physical activities.")

# Footer
st.write("For educational purposes only. Always consult a medical professional.")
