import streamlit as st
import requests

st.title("AI Predictive Maintenance Dashboard")

sensor_2 = st.number_input("Sensor 2", value=518.67)
sensor_3 = st.number_input("Sensor 3", value=643.02)
sensor_4 = st.number_input("Sensor 4", value=1585.29)
sensor_7 = st.number_input("Sensor 7", value=1400.60)
sensor_11 = st.number_input("Sensor 11", value=47.47)
sensor_12 = st.number_input("Sensor 12", value=521.66)
sensor_15 = st.number_input("Sensor 15", value=2388.0)

if st.button("Predict Failure"):

    payload = {
        "sensor_2": sensor_2,
        "sensor_3": sensor_3,
        "sensor_4": sensor_4,
        "sensor_7": sensor_7,
        "sensor_11": sensor_11,
        "sensor_12": sensor_12,
        "sensor_15": sensor_15
    }

    response = requests.post(
        "http://localhost:8081/api/predict",
        json=payload
    )

    result = response.json()

    if result["prediction"] == 1:
        st.error("⚠ Failure Risk Detected")
    else:
        st.success("✅ Engine Healthy")

    st.write(result)