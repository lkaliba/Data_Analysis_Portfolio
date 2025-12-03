# Procedure Pricing Optimization Model

**Author:** Logan Kaliba

**Date:** Nov 3, 2025

## Overview

This project develops a **Mixed-Integer Linear Programming (MILP)** optimization model using **Pyomo** to recommend cost-effective, fairness-constrained reimbursement prices for healthcare procedures. The model was created for a simulated version of the **Blue Cross Louisiana Healthcare Price & Transparency** framework, demonstrating how advanced optimization can support payer decision-making and regulatory compliance.

The model structures provider–procedure pricing, enforces fairness rules across regions, validates constraints, and calculates optimal spending reductions relative to a baseline. A presentation accompanies the notebook to communicate results, methodology, and business impact to non-technical stakeholders.

## Tools & Technologies

* **Python (Pyomo):** Optimization modeling
* **CBC Solver:** MILP solution engine
* **Pandas / NumPy:** Data preparation and validation
* **PowerPoint:** Presentation of results and recommendations
* **Jupyter Notebook:** Full implementation and analysis

## Business Problem

Healthcare payers face rising costs, provider variability, and transparency regulations. The challenge is to:

* Set **fair and consistent reimbursement prices**
* Maintain **regional fairness spreads**
* Ensure **compliance with legal pricing bands**
* Reduce total spending without undermining provider relationships

This model demonstrates how optimization can systematically balance these priorities.

## Optimization Questions Answered

* What are the **optimal reimbursement prices** for each provider and procedure while maintaining fairness across regions?
* How much **total cost savings** can be achieved relative to baseline spending?
* Which providers should be placed in **higher vs. lower price tiers**?
* Do the resulting prices satisfy all fairness and legal constraints?

## Optimization Model Summary

**Objective:**
Minimize total reimbursement spending across all procedures and providers.

**Decision Variables:**

* `x[i,p]` — price paid to provider *i* for procedure *p*
* `a[i,p,t]` — binary variable assigning provider *i* to tier *t*
* `x_min[p,r]`, `x_max[p,r]` — fairness bounds (regional floor and ceiling)

**Key Constraints:**

* Exactly one price tier per provider per procedure
* Prices must fall within legal compliance ranges
* Regional price spreads cannot exceed fairness caps
* Provider minimums & threshold rules enforced
* Total optimized spend must meet or beat savings target

## Key Insights

Using a small simulated dataset (for demonstration):

* **Baseline Spend:** $1,710,000
* **Optimized Spend:** $1,568,000
* **Total Savings:** $142,000 (8.3%)
* Providers in lower tiers achieve most cost reductions
* All fairness constraints remained satisfied (e.g., MRI spread capped at $100 vs a $150 max)

These results show that **MIP optimization offers a scalable, transparent method** for designing reimbursement schedules grounded in fairness and regulation.

## Limitations & Next Steps

**Limitations**

* Tiny dataset for demonstration — real models must scale to hundreds of providers
* Does not incorporate quality ratings or multi-procedure interactions

**Next Steps**

* Integrate real transparency file data
* Add regional and specialty-specific fairness constraints
* Incorporate quality metrics into tier assignment
* Build a dashboard for scenario analysis

## Project Files

| File                                                                                                                   | Description                                                      |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| [`Procedure_Pricing_Optimization_Model_Logan_Kaliba.ipynb`](./Procedure_Pricing_Optimization_Model_Logan_Kaliba.ipynb) | Full Pyomo MILP model, solver setup, and results                 |
| [`Pricing Optimization Presentation`](./Procedure_Pricing_Optimization_Model_Presentation.pptx)                        | PowerPoint explaining model logic, insights, and recommendations |

## What I Learned

* How to structure MILP problems using Pyomo
* Designing fairness constraints for healthcare economics
* Translating complex optimization logic into business-ready storytelling
* Setting solver parameters (MIP gap, time limits) for real-world constraints
* How to build explainable models for non-technical stakeholders

---

*For more projects, visit the main portfolio: [Back to Portfolio](../README.md)*
