# Product Pricing & Profitability Analysis  
**Author:** Logan Kaliba  
**Date:** June 29, 2025

## Overview  
This project evaluates pricing strategy and product profitability for a fictional retail company. The goal was to identify deviations from a standardized markup policy, assess sales growth, and recommend strategic pricing adjustments.

Using SQL in Snowflake, I analyzed product-level sales and cost data to determine which SKUs were mispriced and whether any were being sold at a loss. I presented my insights using PowerPoint and developed an interactive pricing tool in Streamlit as a follow-up to help better understand product information.

## Tools & Technologies  
- **SQL (Snowflake):** Data querying and profitability analysis  
- **Python (Streamlit):** Interactive pricing tool simulation  
- **PowerPoint:** Stakeholder-ready presentation of insights  

## Business Questions Answered  
- What was the year-over-year sales growth between 2022 and 2023?  
- Are any products being sold at a loss?  
- Which products deviate from the company’s standard 50% markup policy?  
- What pricing strategy changes can help improve competitiveness and margin?

## Key Insights  
- **Sales grew 90.7%** from 2022 to 2023, indicating strong growth.  
- **No products** were sold at a loss, suggesting base-level pricing compliance.  
- **13 products** had significant deviations from the expected markup.  
- Mispriced products represent missed revenue or margin optimization opportunities.

## Recommendations  
- Begin price tracking for 3–4 underperforming products as a pilot benchmarking initiative.  
- Establish a **monthly pricing review process** to prevent long-term mispricing while avoiding overcorrections.  
- Integrate third-party competitor pricing data from platforms like **Snowflake Marketplace** to inform pricing decisions.

These steps are designed to support dynamic pricing strategies while maintaining customer trust and revenue integrity.

## Project Files  
| File | Description |
|------|-------------|
| [`Database Setup`](https://github.com/lkaliba/Data_Analysis_Portfolio/blob/main/return_policy_order_analysis/database_setup.sql) | Sets up the Urban Hamster database schema (shared with Return Policy project) |
| [`SQL Queries`](./SQL_queries.sql) | SQL queries to the business questions |
| [`Product Pricing Tool (Streamlit App)`](./product_pricing_tool.py) | Python code for interactive pricing tool built using Streamlit |

## Presentation Videos  
- [Case Study Presentation: Product Pricing & Profitability](https://go.screenpal.com/watch/cT10XunXJyF)  
- [Streamlit App Demo: Product Pricing Tool](https://go.screenpal.com/watch/cT1vlrnl1pB)

## What I Learned  
- How to detect pricing policy violations using SQL logic and arithmetic joins  
- The role of **data-driven storytelling** in business decision-making  
- How **interactive tools** like Streamlit can empower real-time what-if scenario testing for business users
