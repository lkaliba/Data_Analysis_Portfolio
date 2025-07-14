# Scooter Rental Data Analysis
**Author:** Logan Kaliba  
**Date:** March 6, 2025

This project explores a dataset of scooter rentals and analyzes how weather and time-related features affect ridership. It includes visualizations and a simple linear regression model to predict scooter demand (rentals_totals) during specific weather conditions (temp_norm).

## Overview
- Dataset: 731 records of daily scooter rentals
- Columns include: temperature, humidity, workday indicators, season, and rental counts
- Goal: Understand patterns and build a predictive model

## Tools Used
- **Python** (Pandas, Seaborn, Scikit-Learn)
- **Jupyter Notebook** for development
- **Seaborn** for visualizations
- **LinearRegression** from Scikit-Learn for modeling

## Key Insights
- **Temperature is positively correlated** with total rentals (r ≈ 0.63)
- **Winter sees the lowest rental activity**
- **Linear Regression Model** was able to predict rentals based on temperature with a reasonable R² score (0.37)

## Files
- [`scooter_analysis.py`](./scooter_analysis.py) – Python script
- [`scooter_analysis.ipynb`](https://nbviewer.org/github/lkaliba/Data_Analysis_Portfolio/blob/main/scooter_rental_analysis/scooter_analysis.ipynb) – Jupyter Notebook version [view the notebook on NBViewer]
- [`scooter_analysis_report.pdf`](https://raw.githubusercontent.com/lkaliba/Data_Analysis_Portfolio/main/scooter_rental_analysis/scooter_analysis_report.pdf
) – PDF of Jupyter Notebook 

## Model Summary
The regression equation: rentals_total = 1,327.93 + (6,463.97 * temp_norm)

The model can estimate scooter rental demand based on weather temperature.

## What I Learned
- How to clean, rename, and transform real-world datasets
- How to generate meaningful visualizations to communicate insights
- How to build and evaluate a basic machine learning model in Python

---

*For more projects, check out the main portfolio: [Back to Portfolio](../README.md)*
