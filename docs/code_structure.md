# Code Structure

The AgroAlert Ghana source code is organized into modular components representing the complete drought prediction pipeline.

## Data Collection

src/data_collection/

Handles acquisition of:

- Satellite vegetation indices
- Climate variables
- Environmental observations

## Data Processing

src/processing/

Responsible for:

- Data cleaning
- Feature engineering
- Dataset preparation

## Machine Learning Models

src/model/

Contains:

- Random Forest drought classifier
- LSTM temporal forecasting model
- Ensemble prediction framework

## Alert System

src/alerts/

Manages:

- SMS notification workflow
- Voice alert generation
- Farmer communication pipeline

## Dashboard

src/dashboard/

Contains visualization components for:

- Risk monitoring
- Prediction visualization
- System demonstration

## Scheduler

Scheduler.py

Coordinates automated execution of the prediction pipeline.