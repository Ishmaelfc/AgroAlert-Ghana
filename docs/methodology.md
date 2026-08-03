# AgroAlert Ghana Methodology

## 1. Research Overview

AgroAlert Ghana is an artificial intelligence-powered drought prediction and multilingual voice alert framework designed to support smallholder farmers through localized climate risk information.

The system integrates satellite remote sensing, climate reanalysis data, machine learning models and mobile communication technologies to develop a hyperlocal drought early warning approach suitable for agricultural communities in Ghana.

The research workflow consists of five major stages:

1. Environmental data acquisition
2. Data preprocessing and feature engineering
3. Machine learning model development
4. Drought risk prediction
5. Farmer alert delivery and feedback collection

---

# 2. Data Acquisition

The system integrates three major environmental data sources.

## 2.1 Sentinel-2 Satellite Data

Sentinel-2 imagery is processed through Google Earth Engine to extract vegetation information.

The Normalized Difference Vegetation Index (NDVI) is calculated to measure vegetation health and identify changes associated with drought stress.

Key processing steps:

- Cloud filtering
- Community-level spatial extraction
- NDVI calculation
- Weekly aggregation

---

## 2.2 Climate Data

Weather variables are obtained from ERA5 reanalysis data through Open-Meteo.

The following variables are incorporated:

- Rainfall
- Maximum temperature
- Minimum temperature
- Relative humidity
- Reference evapotranspiration (ET0)

These variables provide information about atmospheric and water availability conditions.

---

## 2.3 Land Surface Temperature Data

MODIS MOD11A2 data is used to obtain land surface temperature measurements.

The dataset provides additional information about thermal stress conditions affecting vegetation and agricultural productivity.

---

# 3. Dataset Preparation

All environmental datasets are converted into a weekly temporal resolution.

The final dataset consists of:

- 15 farming communities
- 2019–2023 observation period
- 3,915 weekly observations

Missing satellite observations caused by cloud cover and revisit limitations are handled through:

- Linear interpolation
- Boundary filling methods

---

# 4. Drought Label Construction

Drought events are identified using a combined environmental condition approach.

A drought label is assigned when:

- SPEI proxy < -1.0
- NDVI anomaly < -0.05

This approach identifies periods where both water stress and vegetation stress occur.

The final dataset contains:

- 57 drought-labelled weeks
- 1.5% drought event prevalence

---

# 5. Feature Engineering

To prevent target construction leakage, variables directly used to create drought labels are excluded from model inputs.

The final independent feature set contains:

- Community encoding
- Region encoding
- Raw NDVI
- Rainfall
- Maximum temperature
- Minimum temperature
- Humidity
- Reference evapotranspiration
- Land surface temperature

---

# 6. Machine Learning Development

Two machine learning approaches are developed.

## 6.1 Random Forest Model

Random Forest is selected due to its ability to capture nonlinear relationships within environmental datasets.

Configuration:

- 200 decision trees
- Maximum tree depth of 10
- Balanced class weighting

---

## 6.2 Long Short-Term Memory Network

A Long Short-Term Memory (LSTM) neural network is developed to capture temporal climate patterns.

Architecture:

- Two LSTM layers
- 64 hidden units per layer
- Four-week sequence window
- Dropout regularization

---

# 7. Hybrid Ensemble Model

The Random Forest and LSTM predictions are combined through a weighted ensemble approach.

The final drought probability is calculated using:

Hybrid Score = 0.4 × LSTM Probability + 0.6 × Random Forest Probability

The weighting factor is selected using validation-based optimization.

---

# 8. Model Evaluation

The models are evaluated using temporal validation.

Training period:

2019–2021

Testing period:

2022–2023

Due to the highly imbalanced drought dataset, Precision-Recall Area Under Curve (PR-AUC) is used as the primary evaluation metric.

Additional evaluation methods include:

- ROC-AUC
- Precision
- Recall
- F2-score optimization
- Bootstrap confidence intervals

---

# 9. Alert Delivery Framework

The prediction output is converted into farmer-facing alerts.

Communication channels include:

## Voice Alerts

AI-generated voice calls are used to support farmers with limited literacy.

Supported languages:

- Twi
- Ewe
- Dagbani

## SMS Alerts

Text-based alerts are provided for:

- Literate farmers
- Agricultural extension officers
- Researchers

---

# 10. Farmer Feedback System

A feedback mechanism is integrated to collect field observations after alerts.

Farmers provide drought confirmation through:

- Keypad responses
- SMS feedback

The collected information provides a pathway for future improvement of drought labels and model retraining.

---

# 11. Future Development

Future improvements include:

- Integration of independent drought ground-truth datasets
- Expansion of farmer validation studies
- Additional local language support
- Larger-scale deployment testing
- Operational agricultural advisory partnerships