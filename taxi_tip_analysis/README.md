# 🚕 Taxi Tip Comparison
**Author:** Logan Kaliba  
**Date:** February 13, 2025

## 🧠 Project Overview
This project aims to analyze whether there's a significant difference in the **average tip amount** between **yellow cabs** and **green cabs** in New York City. This project uses a **2-sample t-test** to determine statistical significance.

## 🔍 Tools Used
- Python (Pandas, SciPy, Seaborn)
- Jupyter Notebook
- PDF Report for distribution

## 📊 Summary of Analysis
1. **Data Loading & Exploration**
2. **Data Segmentation**: Split by cab color
3. **Normality Check** using `scipy.stats.normaltest`
4. **Equal Variance Check** using `scipy.stats.bartlett`
5. **2-Sample T-Test** using `scipy.stats.ttest_ind`

### ✅ Result:
- **p-value = 0.963**
- Conclusion: **Fail to reject the null hypothesis** → There is **no statistically significant difference** in the average tip amount between green and yellow cabs.

## 📁 Files Included
- [`taxi_tip_analysis.py`](./taxi_tip_analysis.py) – Clean Python script version
- [`taxi_tip_analysis.ipynb`](https://nbviewer.org/github/lkaliba/Data_Analysis_Portfolio/blob/main/taxi_tip_analysis/taxi_tip_analysis.ipynb) – Full notebook analysis [view notebook on NBViewer]    
- [`taxi_tip_report.pdf`](https://raw.githubusercontent.com/lkaliba/Data_Analysis_Portfolio/main/taxi_tip_analysis/taxi_tip_report.pdf
) – Exported notebook for easy viewing   

## 💡 What I Learned
- How to conduct a proper 2-sample t-test in Python  
- Importance of checking assumptions (normality and variance)  
- Communicating statistical results in a business-friendly way

