import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io

data = """OrderID	CustomerID	Product	Category	Price	Quantity	Region
1	101	Laptop	Electronics	50000	1	West
2	102	Phone	Electronics	20000	2	North
3	101	Mouse	Accessories	500	3	West
4	103	Laptop	Electronics	50000	1	South
5	104	Tablet	Electronics	30000	1	East
6	102	Mouse	Accessories	500	1	North
7	105	Laptop	Electronics	50000	2	West
8	106	Keyboard	Accessories	1500	2	South
9	103	Phone	Electronics	20000	1	South
10	104	Laptop	Electronics	50000	1	East"""

df = pd.read_csv(io.StringIO(data),sep="\s+")
# print(df)

# making this columns 
# Revenue = Price * Quantity
# Tax = Revenue * 0.18
# FinalPrice = Revenue + Tax  

df["Revenue"] = df["Price"]* df["Quantity"]
df["Tax"] = df["Revenue"] * 0.18
df["FinalPrice"] = df["Revenue"] + df['Tax']

# print(df)

# Creating order category
df["OrderCategory"] = np.select([df["Revenue"]<2000,df["Revenue"]<=40000],["small Order","Medium order"],default="Large order")
# print(df)

#Find total revenue per customer.
result = df.groupby("CustomerID")["Revenue"].sum().to_frame(name="Total_revnue")
result["Rank"] = result["Total_revnue"].rank(ascending=False,method="dense")
result = result.sort_values("Rank")
# print(result)

#CreateColumn
df["CustomerTotalRevnue"] = df.groupby("CustomerID")["Revenue"].transform("sum")
# print(df)
# print(df["CustomerTotalRevnue"])

#Create Region vs Product table.
freq_produvt_per_Region = pd.crosstab(df["Region"],df["Product"])
# print(freq_produvt_per_Region)

# Create pivot table:
vot = pd.pivot_table(
    df,
   index= "Category",
   columns= "Region",
   values= "Revenue",
   aggfunc=np.sum,
   fill_value=0
)
print(vot)

#Percentile Analysis

percentiles = np.percentile(df["Revenue"],[25,50,90])

rev_25 = percentiles[0]
rev_50 = percentiles[1]
rev_90 = percentiles[2]

print(f"\n 25th percentile revenue: {rev_25:,.2f}")
print(f"\n 50th percentile revenue: {rev_50:,.2f}")
print(f"\n 90th percentile revenue: {rev_90:,.2f}")

#Simulate sales trend.
df=df.sort_values(by="OrderID")
df["rolling_average_revenue"] =  df["Revenue"].rolling(window=3).mean()
print(df["rolling_average_revenue"])

print(df)