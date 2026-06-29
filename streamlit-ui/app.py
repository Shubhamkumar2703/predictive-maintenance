import streamlit as st
import requests
import pandas as pd

# Sidebar
st.sidebar.title("Predictive Maintenance")
st.sidebar.write("AI Powered Monitoring System")

# Title
st.title("AI Predictive Maintenance Dashboard")

# Inputs
sensor_2 = st.number_input("Sensor 2", value=518.67)
sensor_3 = st.number_input("Sensor 3", value=643.02)
sensor_4 = st.number_input("Sensor 4", value=1585.29)
sensor_7 = st.number_input("Sensor 7", value=1400.60)
sensor_11 = st.number_input("Sensor 11", value=47.47)
sensor_12 = st.number_input("Sensor 12", value=521.66)
sensor_15 = st.number_input("Sensor 15", value=2388.0)

# Predict Button
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
        "https://predictive-maintenance-hzxk.onrender.com/predict",
        json=payload
    )

    result = response.json()

    # Prediction Result
    st.metric(
        label="Prediction Result",
        value=result["status"]
    )

    # Health Score
    if result["prediction"] == 1:
        health = 25
        st.error("⚠ Failure Risk Detected")
    else:
        health = 92
        st.success("✅ Engine Healthy")

    st.metric("Engine Health %", f"{health}%")

# History Section
st.subheader("Prediction History")

history_response = requests.get(
    "https://predictive-maintenance-hzxk.onrender.com/api/history"
)

history = history_response.json()

df = pd.DataFrame(history)

st.dataframe(df)

# Chart
st.subheader("Prediction Distribution")

chart_data = df["prediction"].value_counts()

st.bar_chart(chart_data)

st.subheader("Bulk Prediction using CSV")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    bulk_df = pd.read_csv(uploaded_file)

    st.write("Uploaded Data")
    st.dataframe(bulk_df)

    predictions = []

    for index, row in bulk_df.iterrows():

        payload = {
            "sensor_2": row["sensor_2"],
            "sensor_3": row["sensor_3"],
            "sensor_4": row["sensor_4"],
            "sensor_7": row["sensor_7"],
            "sensor_11": row["sensor_11"],
            "sensor_12": row["sensor_12"],
            "sensor_15": row["sensor_15"]
        }

        response = requests.post(
            "https://predictive-maintenance-hzxk.onrender.com/predict",
            json=payload
        )

        result = response.json()

        predictions.append(result["status"])

    bulk_df["Prediction"] = predictions

    st.subheader("Prediction Results")

    st.dataframe(bulk_df)