# Model Architecture

## Overview

AgroAlert Ghana uses a hybrid machine learning architecture that combines a Random Forest classifier and a Long Short-Term Memory (LSTM) neural network to predict drought risk.

The system is designed to capture both:

- Nonlinear relationships between environmental variables
- Temporal patterns within climate and vegetation data

The complete prediction pipeline consists of four major stages:

1. Environmental feature preparation
2. Individual model prediction
3. Hybrid ensemble combination
4. Risk classification and alert generation

---

# 1. Input Feature Layer

The model receives nine independent environmental features.

| Feature | Description |
|---|---|
| Community encoding | Geographic identifier |
| Region encoding | Administrative location information |
| Raw NDVI | Vegetation condition indicator |
| Rainfall | Precipitation availability |
| Maximum temperature | Heat stress indicator |
| Minimum temperature | Temperature variability |
| Humidity | Atmospheric moisture condition |
| ET0 | Reference evapotranspiration |
| Land Surface Temperature | Surface thermal condition |

Variables directly used in drought label construction are excluded from the model input to reduce target leakage.

---

# 2. Random Forest Model

## Description

Random Forest is used as a baseline machine learning model because of its ability to learn complex nonlinear relationships from environmental data.

## Configuration

| Parameter | Value |
|---|---|
| Number of trees | 200 |
| Maximum depth | 10 |
| Class weighting | Balanced |

The model produces a drought probability score based on current environmental conditions.

---

# 3. LSTM Model

## Description

A Long Short-Term Memory neural network is implemented to capture time-dependent relationships in climate and vegetation patterns.

Unlike traditional machine learning models, LSTM networks process sequential observations and learn patterns occurring across multiple weeks.

## Architecture

| Component | Configuration |
|---|---|
| Network type | LSTM |
| Number of layers | 2 |
| Hidden units | 64 per layer |
| Sequence length | 4 weeks |
| Dropout | 0.30 |
| Output | Sigmoid probability |

The model generates a drought probability score from recent environmental sequences.

---

# 4. Hybrid Ensemble Model

The final AgroAlert Ghana prediction combines outputs from both models.

The hybrid probability is calculated as:

```
Hybrid Score = 0.4 × LSTM Probability + 0.6 × Random Forest Probability
```

The weighting factor was selected using validation-based optimization.

The ensemble combines:

- Random Forest strength in structured environmental data
- LSTM capability for temporal pattern recognition

---

# 5. Model Training Strategy

The dataset is divided using temporal validation.

## Training Period

2019–2021

## Testing Period

2022–2023

This approach simulates real-world deployment where future drought conditions are predicted using historical information.

---

# 6. Model Evaluation

Because drought events represent a small percentage of observations, Precision-Recall Area Under Curve (PR-AUC) is selected as the primary evaluation metric.

Additional metrics include:

- ROC-AUC
- Precision
- Recall
- F2-score
- Bootstrap confidence intervals

---

# 7. Decision Threshold Optimization

The default classification threshold of 0.5 results in poor drought detection due to severe class imbalance.

A recall-oriented threshold is selected using F2-score optimization.

This approach prioritizes detecting drought events because missed warnings have higher consequences for farmers than false alarms.

---

# 8. Alert Generation Pipeline

The final prediction workflow is:

```
Satellite Data
       |
Climate Data
       |
Feature Engineering
       |
Machine Learning Models
       |
Hybrid Ensemble
       |
Drought Risk Score
       |
Threshold Decision
       |
Voice/SMS Alert
       |
Farmer Feedback
```

---

# 9. Future Improvements

Future model development will focus on:

- Integration of independent drought observations
- Larger historical datasets
- Additional deep learning architectures
- Continuous retraining using farmer feedback
- Expansion to additional agricultural regions