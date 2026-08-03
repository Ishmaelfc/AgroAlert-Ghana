# AgroAlert Ghana

## AI-Powered Hyperlocal Drought Prediction and Multilingual Voice Alert System for Smallholder Farmers Using a Hybrid Random Forest–LSTM Ensemble

<p align="center">
A research-driven climate intelligence framework integrating satellite remote sensing, climate data, machine learning and inclusive communication technologies for drought early warning in Ghana.
</p>

---

## Overview

Climate change is increasing drought frequency and severity across Ghana, creating significant risks for smallholder farmers who depend on rain-fed agriculture.

Many existing drought monitoring systems provide regional-scale information but often fail to deliver timely, localized and accessible warnings to rural communities, particularly farmers with limited digital access or literacy.

AgroAlert Ghana presents an artificial intelligence-powered hyperlocal drought prediction and multilingual alert framework designed to bridge the gap between climate information and last-mile agricultural decision-making.

The system combines:

- Satellite remote sensing
- Climate reanalysis data
- Machine learning prediction
- Multilingual voice communication
- Farmer feedback mechanisms

The current implementation demonstrates the technical feasibility of an AI-driven drought early warning system for smallholder farming communities in Ghana.

---

# Research Objectives

The project aims to:

- Develop a hyperlocal drought prediction framework using environmental data and machine learning.
- Integrate satellite observations and climate variables for drought risk assessment.
- Compare Random Forest, LSTM and hybrid ensemble approaches.
- Develop an inclusive farmer alert mechanism using voice and SMS communication.
- Establish a feedback loop for future model improvement.

---

# Key Contributions

The major contributions of AgroAlert Ghana include:

### 1. Hybrid Machine Learning Framework

A hybrid Random Forest–LSTM ensemble was developed by combining:

- Random Forest capability for environmental tabular data modelling.
- LSTM capability for capturing temporal climate patterns.

The ensemble combines both model outputs using validation-selected weighting.

---

### 2. Leakage-Controlled Drought Prediction Pipeline

The study addresses target construction leakage by excluding drought-label-derived variables from model inputs.

The final model uses nine independent environmental features:

- Community encoding
- Region encoding
- NDVI
- Rainfall
- Maximum temperature
- Minimum temperature
- Humidity
- Reference evapotranspiration (ET0)
- Land surface temperature

---

### 3. Hyperlocal Climate Monitoring

The framework was evaluated across:

- 15 farming communities
- All 16 administrative regions of Ghana
- Weekly observations from 2019–2023

---

### 4. Inclusive Farmer Communication

The alert system supports farmers through:

- AI-generated voice calls
- SMS notifications

Supported voice languages:

- Twi
- Ewe
- Dagbani

This approach prioritizes accessibility for farmers with limited literacy or internet connectivity.

---

# System Architecture

AgroAlert Ghana consists of five major layers:
Environmental Data Sources
|
↓
Data Processing & Feature Engineering
|
↓
Hybrid Random Forest–LSTM Prediction Engine
|
↓
Alert Generation System
|
↓
Farmer Feedback and Model Improvement

# Data Sources

## Sentinel-2 Satellite Imagery

Processed through Google Earth Engine.

Used for:

- NDVI extraction
- Vegetation condition monitoring

---

## ERA5 Weather Reanalysis

Retrieved through Open-Meteo.

Variables include:

- Rainfall
- Temperature
- Humidity
- Reference evapotranspiration

---

## MODIS MOD11A2 Land Surface Temperature

Used for:

- Surface temperature monitoring
- Heat stress analysis

---

# Dataset Summary

Final dataset:

| Parameter | Description |
|---|---|
| Observation period | 2019–2023 |
| Communities | 15 |
| Weekly observations | 3,915 |
| Drought-labelled weeks | 57 |
| Drought prevalence | 1.5% |

---

# Machine Learning Framework

## Random Forest

Configuration:

- 200 decision trees
- Maximum depth: 10
- Balanced class weighting


## LSTM Network

Architecture:

- Two LSTM layers
- 64 hidden units per layer
- Four-week temporal sequence window
- Dropout regularization


## Hybrid Ensemble

The final drought probability is calculated using:
Hybrid Score =
0.4 × LSTM Probability
+
0.6 × Random Forest Probability
The ensemble weight was selected through validation-based optimization.

---

# Model Evaluation

The study uses temporal validation:

Training:
2019-2021

Testing:
2022-2023
The primary evaluation metric is:

Precision-Recall Area Under Curve (PR-AUC)

This metric was selected because drought events represent a highly imbalanced classification problem.

---

# Results

| Model | PR-AUC |
|---|---:|
| Random Forest | 0.165 |
| LSTM | 0.156 |
| Hybrid RF-LSTM Ensemble | 0.170 |

The hybrid model achieved the highest point estimate while acknowledging statistical uncertainty due to the limited number of observed drought events.

A recall-oriented decision threshold using F2-score optimization improved drought detection performance compared with the default classification threshold.

---

# Alert Delivery Framework

The communication layer provides:

## Voice Alerts

Designed for farmers with limited literacy.

Languages:

- Twi
- Ewe
- Dagbani


## SMS Alerts

Designed for:

- Literate farmers
- Agricultural extension officers
- Researchers

---

# Farmer Feedback Mechanism

A proof-of-concept feasibility test was conducted with registered farmers.

The feedback mechanism allows farmers to:

- Confirm drought conditions
- Report observations
- Support future model improvement

Collected responses provide a pathway toward future ground-truth dataset development.

---

## Repository Structure

The repository is organized into modules for data management, model development, evaluation and documentation.

| Folder/File | Description |
|---|---|
| data/ | Satellite, climate and processed datasets used in the research |
| data/raw/ | Original datasets collected from external sources |
| data/processed/ | Cleaned and prepared datasets used for modelling |
| notebooks/ | Jupyter notebooks for analysis, experiments and evaluation |
| src/ | Core Python scripts for data processing, modelling and deployment |
| models/ | Saved machine learning models and model configurations |
| figures/ | Research figures, system diagrams and visualization outputs |
| results/ | Model performance metrics, predictions and analysis reports |
| docs/ | Research documentation and supporting materials |
| assets/ | Images and repository graphics |
| requirements.txt | Python packages required to run the project |
| CITATION.cff | Citation metadata for academic referencing |
| LICENSE | Repository usage and distribution terms |
| README.md | Project overview and documentation |


---

# Future Development Roadmap

## Phase 1: Research Validation 

Completed:

- Satellite data integration
- Climate feature engineering
- Hybrid machine learning development
- Feasibility testing


## Phase 2: Expanded Validation

Future work:

- Integration of independent drought ground-truth datasets
- Larger farmer feedback studies
- Additional local language support
- Multi-season validation


## Phase 3: Operational Deployment

Future opportunities:

- Partnership with agricultural organizations
- Scalable cloud deployment
- Real-time farmer advisory services

---

# Limitations

Current limitations include:

- Limited number of observed drought events.
- Need for independent drought ground-truth records.
- Small-scale farmer feedback validation.
- Additional language support required for nationwide coverage.

---

# Publication

AgroAlert Ghana: A Hyperlocal Drought Prediction and Multilingual Voice Alert System for Smallholder Farmers Using a Hybrid Random Forest–LSTM Ensemble

Authors:

- Ishmael Fynn Cudjoe
- Anastasia Oheneba Duah

Department of Electrical and Electronic Engineering  
University of Mines and Technology (UMaT), Tarkwa, Ghana

---

# Citation

If you use this work for academic purposes, please cite:
Cudjoe, I. F., & Duah, A. O.

AgroAlert Ghana: A Hyperlocal Drought Prediction and Multilingual Voice Alert System for Smallholder Farmers Using a Hybrid Random Forest–LSTM Ensemble.