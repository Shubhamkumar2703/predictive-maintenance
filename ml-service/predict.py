from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Create app
app = FastAPI()

# Load files
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")

# Input schema
class SensorData(BaseModel):
    sensor_2: float
    sensor_3: float
    sensor_4: float
    sensor_7: float
    sensor_11: float
    sensor_12: float
    sensor_15: float

# API endpoint
@app.post("/predict")
def predict(data: SensorData):

    input_data = np.array([
        [
            data.sensor_2,
            data.sensor_3,
            data.sensor_4,
            data.sensor_7,
            data.sensor_11,
            data.sensor_12,
            data.sensor_15
        ]
    ])

    # Scale
    scaled_data = scaler.transform(input_data)

    # Predict
    prediction = model.predict(scaled_data)[0]

    # Response
    return {
        "prediction": int(prediction),
        "status": "Failure Risk" if prediction == 1 else "Healthy"
    }