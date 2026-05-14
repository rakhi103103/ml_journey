# E-Commerce Churn Analysis — SQL Project
**Tool:** MySQL 8.0 | **Data:** Olist Brazilian E-Commerce (Kaggle)

## What I was trying to answer
An e-commerce business has thousands of customers — but how many 
actually come back? I used real Brazilian order data to find out 
who churned, when, and how much revenue was lost.

## Data used
- orders — 99,441 rows
- customers — 99,441 rows  
- payments — 103,886 rows

## What I practised
- LAG() and DATEDIFF() to calculate gaps between purchases
- Chained CTEs to label and count churned customers
- 3-table JOINs to connect orders, customers and payments
- DATE_FORMAT() for monthly trend analysis
- CASE WHEN for customer segmentation

## What I found
- 80.57% of customers never came back after their first order
- Churned customers spent 4x more than active ones — ₹1.23 crore lost
- November 2017 had the biggest spike — likely Black Friday
- São Paulo dominates revenue but has smallest average order value
- 78% of all payments are by credit card

## Files
- `ecommerce_churn.sql` — 12 queries with comments
- `import_data.py` — loads the CSVs into MySQL