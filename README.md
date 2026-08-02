# AgroAlert Ghana

## AI-Powered Hyperlocal Drought Prediction and Multilingual Voice Alert System for Smallholder Farmers

## Overview

AgroAlert Ghana is an artificial intelligence-based drought early warning system developed to support smallholder farmers in Ghana.

The project combines satellite remote sensing data, climate information and machine learning models to predict drought conditions at a hyperlocal scale and deliver accessible alerts through voice and SMS communication.

The system was designed to address limitations in conventional drought monitoring approaches, which often provide regional forecasts and fail to reach rural farming communities.

---

## Research Objectives

- Develop a machine learning framework for hyperlocal drought prediction.
- Integrate satellite-derived vegetation indicators with climate variables.
- Provide accessible drought alerts through multilingual voice communication.
- Support climate resilience among smallholder farmers.

---

## System Architecture

The AgroAlert Ghana pipeline consists of:

1. Data Acquisition
   - Sentinel-2 satellite imagery
   - ERA5 climate data
   - MODIS land surface temperature data

2. Data Processing
   - Vegetation index extraction
   - Climate feature engineering
   - Drought indicator generation

3. Machine Learning Prediction
   - Logistic Regression
   - Random Forest
   - Long Short-Term Memory (LSTM)

4. Alert Delivery
   - Voice alerts
   - SMS notifications
   - Farmer feedback mechanism

---

## Dataset

The study used weekly environmental observations generated from multiple climate and satellite datasets.

Features include:

- NDVI anomaly
- Rainfall deficit
- Land surface temperature
- Water balance indicators
- SPEI-based drought indicators

Dataset size:

- 1,575 weekly records
- 15 farming communities across Ghana

---

## Machine Learning Models

### Random Forest

Implementation:
- Python
- Scikit-learn

Configuration:
- 200 estimators
- Maximum depth: 10


### Long Short-Term Memory Network

Implementation:
- Python
- PyTorch

Architecture:
- Four-week temporal lookback sequence

---

## Results

The models were evaluated using drought prediction performance metrics.

Key observations:

- Random Forest demonstrated strong precision-recall performance.
- LSTM captured temporal drought patterns from sequential climate data.
- The framework demonstrated potential for localized drought monitoring.

---

## Technologies Used

### Programming
- Python

### Machine Learning
- Scikit-learn
- PyTorch

### Data Processing
- Google Earth Engine
- Remote sensing analysis

### Visualization
- Matplotlib
- Chart.js

### Communication
- Africa's Talking API

---

## Repository Structure
