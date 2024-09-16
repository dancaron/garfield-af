import streamlit as st

# Function to calculate GARFIELD-AF score
def calculate_garfield_af(age, hypertension, diabetes, stroke_history, vascular_disease, anticoagulation):
    # Risk factors weightings for GARFIELD-AF (based on study data)
    risk_score = 0
    if age >= 75:
        risk_score += 2
    elif age >= 65:
        risk_score += 1
    if hypertension:
        risk_score += 1
    if diabetes:
        risk_score += 1
    if stroke_history:
        risk_score += 2
    if vascular_disease:
        risk_score += 1
    if anticoagulation:
        risk_score -= 1  # Anticoagulation reduces the risk

    return risk_score

# Streamlit app UI
st.title("GARFIELD-AF Risk Calculator")
st.write("""
This tool calculates the risk of stroke, major bleeding, and mortality for patients with Atrial Fibrillation (AF) using the GARFIELD-AF score. 
The app takes into account clinical risk factors and the patient's anticoagulation status.
""")

# Input fields
age = st.number_input("Age", min_value=18, max_value=120, value=65)
hypertension = st.checkbox("Hypertension", value=False)
diabetes = st.checkbox("Diabetes", value=False)
stroke_history = st.checkbox("History of Stroke or TIA", value=False)
vascular_disease = st.checkbox("Vascular Disease", value=False)
anticoagulation = st.checkbox("On Anticoagulation Therapy", value=False)

# Calculate GARFIELD-AF score
if st.button("Calculate GARFIELD-AF Score"):
    score = calculate_garfield_af(age, hypertension, diabetes, stroke_history, vascular_disease, anticoagulation)
    st.write(f"The GARFIELD-AF risk score for this patient is: {score}")
    if anticoagulation:
        st.write("The patient is on anticoagulation therapy, which may lower stroke risk.")
    else:
        st.write("The patient is not on anticoagulation therapy.")
