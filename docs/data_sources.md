# Data Sources and Processing

## Overview

AgroAlert Ghana integrates satellite remote sensing data, climate reanalysis data and communication services to develop a hyperlocal drought prediction and alert framework.

The system combines environmental observations from multiple open-access platforms to generate weekly drought risk predictions for farming communities in Ghana.

---

# 1. Sentinel-2 Satellite Imagery

## Source

**Platform:** Copernicus Sentinel-2 Mission  
**Processing Platform:** Google Earth Engine (GEE)

Sentinel-2 multispectral imagery is used to monitor vegetation conditions through the Normalized Difference Vegetation Index (NDVI).

NDVI provides an indicator of vegetation health and drought-related stress.

## Data Processing

The processing workflow includes:

- Satellite image acquisition through Google Earth Engine
- Cloud filtering
- Community-level spatial extraction
- NDVI computation
- Weekly temporal aggregation

NDVI is extracted within community buffer regions representing the selected farming locations.

---

# 2. ERA5 Climate Reanalysis Data

## Source

**Provider:** European Centre for Medium-Range Weather Forecasts (ECMWF)  
**Access Platform:** Open-Meteo

ERA5 climate data provides atmospheric and hydrological variables required for drought analysis.

## Variables Used

The following variables are included:

| Variable | Purpose |
|---|---|
| Rainfall | Water availability assessment |
| Maximum temperature | Heat stress monitoring |
| Minimum temperature | Climate condition assessment |
| Relative humidity | Atmospheric moisture estimation |
| Reference evapotranspiration (ET0) | Water demand estimation |

## Processing

Climate variables are:

- Retrieved daily
- Aggregated into weekly observations
- Combined with satellite-derived features

---

# 3. MODIS Land Surface Temperature

## Source

**Product:** MOD11A2 Version 6.1  
**Provider:** NASA Earth Observation Program

MODIS Land Surface Temperature (LST) data provides thermal information about surface conditions.

## Processing

The workflow includes:

- Data extraction through Google Earth Engine
- Conversion from digital numbers to temperature values
- Weekly aggregation
- Integration with other environmental variables

LST provides additional information about vegetation and environmental heat stress.

---

# 4. Google Earth Engine

Google Earth Engine is used as the primary remote sensing processing environment.

Applications within AgroAlert Ghana include:

- Sentinel-2 image processing
- NDVI extraction
- MODIS LST processing
- Community-level spatial analysis

The platform enables scalable processing of satellite datasets without requiring local storage of large imagery archives.

---

# 5. Africa's Talking Communication Platform

## Purpose

Africa's Talking is used for the communication layer of AgroAlert Ghana.

The platform supports:

- Voice call delivery
- SMS notifications
- Farmer feedback collection

## Alert Workflow

1. Machine learning model generates drought risk score.
2. Risk level is evaluated using selected decision thresholds.
3. Farmers receive voice or SMS notifications.
4. Farmer responses are collected for future model improvement.

---

# 6. Dataset Summary

| Dataset | Source | Application |
|---|---|---|
| Sentinel-2 | Copernicus | Vegetation monitoring through NDVI |
| ERA5 Weather Data | ECMWF/Open-Meteo | Climate feature generation |
| MODIS MOD11A2 | NASA | Land surface temperature |
| Africa's Talking | Communication API | Voice and SMS alerts |

---

# 7. Data Limitations

The current study identifies several data limitations:

- Satellite observations are affected by cloud coverage.
- Drought labels rely on proxy environmental indicators.
- Independent field-based drought records remain limited.
- Larger farmer feedback datasets are required for future validation.
git
Future development will focus on integrating additional ground observations and expanding community-level monitoring