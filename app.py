import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('model/phishing_model.pkl')

# Streamlit UI
st.title("🔎 AI-Based Phishing Detection System")
st.write("Enter website details below to check if it's **phishing** or **legitimate**.")

# Function to convert Yes/No to 1/-1
def yes_no_to_numeric(option):
    return 1 if option == "Yes" else -1

# Input fields for website features
url_length = st.number_input("URL Length", min_value=0)
having_at_symbol = yes_no_to_numeric(st.radio("Having '@' Symbol", ["Yes", "No"]))
prefix_suffix = yes_no_to_numeric(st.radio("Prefix/Suffix in Domain", ["Yes", "No"]))
ssl_final_state = yes_no_to_numeric(st.radio("SSL Final State (Valid Certificate)", ["Yes", "No"]))
domain_reg_length = st.number_input("Domain Registration Length (in years)", min_value=0)
request_url = yes_no_to_numeric(st.radio("Request URL (Image Links from Different Domain)", ["Yes", "No"]))
submitting_to_email = yes_no_to_numeric(st.radio("Submitting to Email", ["Yes", "No"]))
age_of_domain = st.number_input("Age of Domain (in months)", min_value=0)
web_traffic = st.number_input("Web Traffic (Alexa Rank, Higher = Better)", min_value=0)
google_index = yes_no_to_numeric(st.radio("Google Indexed", ["Yes", "No"]))

# Prediction Logic
if st.button("🔍 Predict"):
    features = np.array([[
        url_length, having_at_symbol, prefix_suffix, 
        ssl_final_state, domain_reg_length, 
        request_url, submitting_to_email, 
        age_of_domain, web_traffic, google_index
    ]])

    # Prediction
    prediction = model.predict(features)[0]
    result = "🚨 **Phishing Website**" if prediction == 1 else "✅ **Legitimate Website**"

    # Display Result
    st.markdown(f"### Prediction: {result}")