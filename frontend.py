import streamlit as st
import requests

# --- Page Config
st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="💰",
    layout="centered"
)

# -- Title
st.title("💰 Insurance Premium Prediction")
st.write("Fill in the details below to predict the insurance premium category.")

st.divider()

# ---- Input Form
with st.form("prediction_form"):

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=25
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0,
        max_value=120.0,
        value=70.0
    )

    height = st.number_input(
        "Height (m)",
        min_value=0.5,
        max_value=2.5,
        value=1.75,
        step=0.01
    )

    income_lpa = st.number_input(
        "Annual Income (LPA)",
        min_value=0.1,
        value=5.0,
        step=0.5
    )

    smoker = st.radio(
        "Smoker",
        ["No", "Yes"]
    )

    city = st.selectbox(
        "City",
        [
            "Delhi",
            "Mumbai",
            "Chennai",
            "Kolkata",
            "Bangalore",
            "Pune",
            "Hyderabad",
            "Jaipur",
            "Lucknow",
            "Bhubaneswar",
            "Other"
        ]
    )

    occupation = st.selectbox(
        "Occupation",
        [
            "private_job",
            "government_job",
            "business_owner",
            "freelancer",
            "student",
            "retired",
            "unemployed"
        ]
    )

    submit = st.form_submit_button("Predict Premium")

# -- Prediction 
if submit:

    payload = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": True if smoker == "Yes" else False,
        "city": city,
        "occupation": occupation
    }

    try:

        response = requests.post(
            "https://insurance-premium-api-y9ht.onrender.com/predict",
            json=payload
        )

        if response.status_code == 200:
            st.success(response.json())

        else:
            st.error("Prediction Failed")
            st.write(response.text)

    except Exception as e:
        st.error("Could not connect to FastAPI server.")
        st.exception(e)