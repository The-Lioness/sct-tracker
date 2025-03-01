# sct-tracker
Real Time Symptom Tracker for Sickle Cell Trait
import streamlit as st

# Title
st.title("Real-Time Symptom Tracker for Sickle Cell Trait")

# Introduction
st.write("""
This tool helps individuals with **Sickle Cell Trait (SCT)** monitor symptoms **during exercise** 
and receive immediate safety recommendations.
""")

# Symptom Selection
st.subheader("Select Your Symptoms")
symptoms = st.multiselect("Choose any symptoms you're experiencing:", [
    "Dizziness",
    "Severe muscle cramps",
    "Shortness of breath",
    "Nausea",
    "Rapid heartbeat",
    "Extreme fatigue",
    "Confusion",
    "Chest pain",
    "None"
])

# Severity Rating
st.subheader("Rate Severity")
severity = st.radio("How severe are your symptoms?", ["Mild", "Moderate", "Severe"])

# Time Exercising Before Symptoms Appeared
time_exercising = st.slider("How many minutes were you exercising before symptoms appeared?", 0, 60, 10)

# Risk Assessment Logic
risk_level = "Low Risk"
if "None" in symptoms or not symptoms:
    risk_level = "No Risk"
elif "Severe muscle cramps" in symptoms or "Shortness of breath" in symptoms or "Chest pain" in symptoms:
    if severity == "Severe":
        risk_level = "High Risk"
    else:
        risk_level = "Moderate Risk"
elif severity == "Moderate":
    risk_level = "Moderate Risk"

# Display Risk Level
st.subheader("Your Risk Level:")
st.write(f"**{risk_level}**")

# Safety Recommendations
st.subheader("Immediate Action Plan:")
if risk_level == "No Risk":
    st.write("✅ You are safe to continue. Stay hydrated and monitor your body.")
elif risk_level == "Low Risk":
    st.write("⚠️ Take a short break, drink water, and stretch. If symptoms worsen, seek help.")
elif risk_level == "Moderate Risk":
    st.write("🚨 Stop exercising immediately. Rest, hydrate, and monitor symptoms.")
elif risk_level == "High Risk":
    st.write("❗ **Seek medical attention immediately!** Stop all activity and get help.")

# Additional Notes
st.write("""
**If symptoms persist or worsen, contact a healthcare provider immediately.**
""")
# Footer
st.write("For educational purposes only. Always consult a medical professional.")
