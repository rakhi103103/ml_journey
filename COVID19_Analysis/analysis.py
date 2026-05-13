import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

daily = pd.read_csv("worldometer_coronavirus_daily_data.csv")
summary = pd.read_csv("worldometer_coronavirus_summary_data.csv")

# print(daily.head())
# print(f"\n\nShapes: {daily.shape}")
# print(f"\n\nColumn Names:\n {daily.columns}")
# print(summary.head())
# print(f"\n\nShapes: {summary.shape}")
# print(f"\n\nColumn Names:\n {summary.columns}")

# #missing values

# missing_daily_value = daily.isnull().sum()
# percentage_daily = (missing_daily_value/len(daily))*100
# missing_summary_value = summary.isnull().sum()
# percentage_summary = (missing_summary_value/len(summary))*100
# print(f"\n\nthe missing value of daily databse are:\n{missing_daily_value}")
# print(f"\n\n The percentage of missig value for daily databse are: \n{percentage_daily}")
# print(f"\n\nthe missing value of summary databse are:\n{missing_summary_value}")
# print(f"\n\n The percentage of missig value for summary databse are: \n{percentage_summary}")

#clean the missing value
columns_to_fix_daily = ["daily_new_cases","active_cases","cumulative_total_deaths","daily_new_deaths"]
daily[columns_to_fix_daily] = daily[columns_to_fix_daily].fillna(0)
columns_to_fix_summary = ["total_recovered","active_cases","total_deaths","total_tests","total_deaths_per_1m_population","total_tests_per_1m_population"]
summary[columns_to_fix_summary]=summary[columns_to_fix_summary].fillna(0)
summary = summary.drop(columns=["serious_or_critical"])
print(f"\n\nAfter cleaning the table\n Daily\n:{daily.isnull().sum()}")
print(f"\n\nAfter cleaning the table\n Summary\n:{summary.isnull().sum()}")

#Convert date column to datetime
daily["date"] = pd.to_datetime(daily["date"])
daily["year"] = daily["date"].dt.year
daily["month"]=daily["date"].dt.month

print(daily[["date","year","month"]].head())

# Top 10 countries by total cases
# Using the summary dataframe
top10_cases = summary.sort_values(by="total_confirmed" , ascending=False)[["total_confirmed","country","total_deaths","population"]].head(10)
print(f"\n\nthe top 10 countries are:\n{top10_cases}")

#Death Rate by Country
summary["death_rate"] = (summary["total_deaths"] / summary['total_confirmed']) * 100
print(f"{summary['death_rate']}")
include = summary[summary["total_confirmed"]>1000]
tp10 = include.nlargest(10,"death_rate")[["country", "total_confirmed", "total_deaths", "death_rate"]]
print(f"top 10 are: {tp10}")

#Total Cases Over Time 
global_daily = daily.groupby("date")["daily_new_cases"].sum().reset_index()
global_daily['rolling_avg'] = global_daily["daily_new_cases"].rolling(7).mean()
print(f"\n\nglobal daily:\n {global_daily}")
print(f"\n\n {global_daily['rolling_avg'].head()}")

#Continent wise analysis
continent_wise = summary.groupby("continent").agg({"total_confirmed":"sum","total_deaths":"sum","total_recovered":"sum"}).reset_index().sort_values(by="total_confirmed",ascending=False)
print(f"\n\n\n{continent_wise}")
