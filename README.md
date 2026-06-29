# AI-Powered Predictive Maintenance System

## Overview

AI-based predictive maintenance system built using Machine Learning, FastAPI, Spring Boot, Streamlit, and MySQL.

The project predicts industrial machine failure risk using real sensor data from the NASA CMAPSS turbofan engine dataset.

---

## Features

* Real-time machine failure prediction
* FastAPI AI inference service
* Spring Boot backend integration
* Interactive Streamlit dashboard
* CSV bulk prediction
* Prediction analytics and charts
* MySQL prediction history storage
* Sensor health monitoring

---

## Tech Stack

### Frontend

* Streamlit
* Pandas
* NumPy

### Backend

* Java
* Spring Boot
* REST APIs
* JPA/Hibernate

### AI/ML

* Python
* FastAPI
* Scikit-learn
* Random Forest Classifier

### Database

* MySQL

---

## Architecture

Streamlit Dashboard
↓
Spring Boot Backend
↓
FastAPI ML Service
↓
Machine Learning Model
↓
MySQL Database

---

## Dataset

NASA CMAPSS Turbofan Engine Dataset

---

## Machine Learning Workflow

1. Load and preprocess NASA CMAPSS dataset
2. Train Random Forest Classifier
3. Save trained model using Joblib
4. Expose prediction API using FastAPI
5. Connect backend with Spring Boot
6. Visualize predictions in Streamlit dashboard

---

## Features Implemented

* AI-based failure prediction
* Real-time REST API integration
* Sensor health analysis
* Prediction history
* CSV upload and bulk prediction
* Interactive dashboard and charts

---

## How to Run Locally

### Start FastAPI

```bash
cd ml-service
python -m uvicorn predict:app --reload
```

### Start Spring Boot

```bash
cd spring-backend/backend
mvn spring-boot:run
```

### Start Streamlit

```bash
cd streamlit-ui
python -m streamlit run app.py
```

---

## Future Improvements

* Docker deployment
* JWT Authentication
* Kafka streaming
* React frontend
* Deep Learning (LSTM)
* Cloud deployment

---

## Author

Shubham Kumar
Jabalpur Engineering College
