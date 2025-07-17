# Return Policy & Order Analysis
**Author:** Logan Kaliba  
**Date:** May 27, 2025

## Overview
This project analyzes customer returns and order trends for **Urban Hamster**, a fictional clothing retailer. The goal was to evaluate the performance of the company’s return policy and identify opportunities for improvement.

Using SQL, I queried a multi-year dataset to identify patterns in return behavior, assess financial impact, and compare Urban Hamster’s performance to industry benchmarks. I also created a presentation to communicate key findings and built an interactive Tableau dashboard as a visual extension of the analysis.

## Tools & Technologies
- **SQL (Snowflake):** Data extraction and analysis  
- **Tableau:** Dashboard creation for order insights  
- **PowerPoint:** Business presentation of findings  

## Business Questions Answered
- What is Urban Hamster’s return rate, and how does it compare to the retail industry average?
- Which products are returned most often, and why?
- How has the return rate changed over time?
- What recommendations can reduce return volume while improving customer experience?

## Key Insights
- Urban Hamster’s **2024 return rate was 10%**, outperforming the **industry average of 13.2%** by over 24%.
- **Pants, leggings, and hosiery** were the most returned categories—likely due to fit and sizing issues.
- Returns led to over **$1 million in lost revenue** over the study period.
- Return volume has **increased steadily year over year**, signaling a need for policy review.

## Recommendations
- Extend the return window to 30 days.
- Accept items in “resalable” (not just pristine) condition.
- Offer free return shipping and return drop-off barcodes.
- Digitize and simplify the return process with online request tools.

These strategies aim to improve trust, increase retention, and reduce cart abandonment.

## Project Files
| File | Description |
|------|-------------|
| [`Database Setup`](./database_setup.sql) | Sets up the Urban Hamster database schema |
| [`SQL Queries`](./SQL_queries.sql) | SQL queries with the answers to my business questions |

## Interactive Tableau Dashboard
**[View the Dashboard (Orders by Brand, Category, and Status)](https://public.tableau.com/views/Ordersby_17488327186010/OrdersDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)**    
The dashboard visualizes order trends by year, product type, and return status. Designed to support inventory planning, vendor evaluation, and fulfillment insights.

## Presentation Videos
- [Order Analysis and Return Policy Recommendations](https://go.screenpal.com/watch/cThtYUn6abe)  
- [Dashboard Walkthrough](https://go.screenpal.com/watch/cT1ehFn6sPQ)  

## What I Learned
- How to turn raw SQL data into compelling business narratives  
- The importance of visual simplicity when communicating technical insights  
- How to align recommendations with stakeholder concerns (cost, experience, loyalty)  
