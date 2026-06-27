import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import joblib

# Column names
columns = [
    'engine_id',
    'cycle',
    'op1',
    'op2',
    'op3'
]

# Add sensor columns
for i in range(1, 22):
    columns.append(f'sensor_{i}')

# LOAD DATASET
df = pd.read_csv(
    "CMAPSSData/train_FD001.txt",
    sep=r"\s+",
    header=None
)

# Remove extra empty columns
df = df.iloc[:, :26]

# Set column names
df.columns = columns

print(df.head())

# Calculate max cycle per engine
max_cycle = df.groupby('engine_id')['cycle'].max()

# Merge max cycle
df = df.merge(
    max_cycle.to_frame(name='max_cycle'),
    on='engine_id'
)

# Remaining useful life
df['RUL'] = df['max_cycle'] - df['cycle']

# Create failure label
df['failure'] = df['RUL'].apply(
    lambda x: 1 if x < 30 else 0
)

# Important sensors
features = [
    'sensor_2',
    'sensor_3',
    'sensor_4',
    'sensor_7',
    'sensor_11',
    'sensor_12',
    'sensor_15'
]

X = df[features]
y = df['failure']

# Scaling
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
preds = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, preds)

print(f"Accuracy: {accuracy}")

# Save model
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(features, "features.pkl")

print("Model saved successfully!")