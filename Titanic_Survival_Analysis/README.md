# 🚢 Titanic Survival Analysis

## What This Project Does
Exploratory data analysis on Titanic passenger data to uncover
survival patterns by gender, class, age and fare.

## Dataset
- Source: Kaggle — Titanic Dataset
- 891 passengers, 12 features

## Skills Used
- **Pandas**: groupby, pivot_table, crosstab, transform, fillna
- **NumPy**: percentile, boolean masking, np.where, np.select
- **Matplotlib**: bar chart, grouped bar, histogram, pie chart

## Key Insights
- Female survival rate: 74% vs Male: 19%
- 1st class passengers survived at 3x the rate of 3rd class
- Top 5 fare payers all travelled in 1st class (max fare: 512)
- 75% of wealthy passengers (top 10% fare) survived

## Files
- analysis.py — full analysis script
- Titanic-Dataset.csv — dataset
- survival_count.png — survival count chart
- survival_by_class_gender.png — grouped bar chart
- age_distribution.png — age histogram
- age_group_pie.png — age group pie chart