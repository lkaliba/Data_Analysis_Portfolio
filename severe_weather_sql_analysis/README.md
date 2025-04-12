# 🌪️ Severe Weather SQL Analysis
**Author:** Logan Kaliba  
**Date:** March 22, 2025

## 📌 Project Overview
This project explores a dataset of **severe weather events** in the United States. Using SQL in a cloud environment (Snowflake), I modeled storm event data and answered real business questions about property damage, storm frequency, source reliability, and event duration.

Each question required thoughtful use of SQL joins, window functions, case statements, and CTEs — combining both technical skill and domain understanding.

## 🧠 Key Questions Answered
1. **Who were the top 5 sources** of weather data?
2. What was the **total property damage** by state and event type?
3. How many days did the **longest event** last?
4. Which event was the **third storm** in Abbeville County, South Carolina?
5. What was the **cumulative damage by month**?
6. Which sources are **major** vs. **minor contributors**?
7. Which states had the **highest storm density** (storms per sq. kilometer)?

## 💡 Tools & Key Techniques Used
1. Snowflake (SQL):
- `DENSE_RANK()` window function
- `CASE WHEN` conditional logic
- `EXTRACT()` from datetime
- `TIMESTAMPDIFF()` for event duration
- `WITH` Common Table Expressions (CTEs)
- S3 integration + file staging + COPY INTO
- Joins between multiple datasets (storm data and state land area)
2. Excel: for storing query results

## 📊 Insights Discovered
- **"Public"** was the most common source of severe weather info.
- **Alabama Flash Floods** caused over **$14M** in damages.
- The **longest single weather event lasted 30 days**.
- The **District of Columbia** had the **highest storm density** in the nation.

## 📁 Files Included
- `severe_weather_sql_analysis.md` – All SQL queries  
- `severe_weather_sql_analysis.xlsx` – Query results and summaries  

## ✅ What I Learned
- How to manage complex data workflows in SQL
- How to perform spatial and temporal analysis
- How to uncover high-impact insights from climate data
  
---

📌 *For more projects, check out the main portfolio: [Back to Portfolio](../README.md)*
