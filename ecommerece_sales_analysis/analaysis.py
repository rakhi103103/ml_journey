import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io

data ="""CustomerID	Product	Price	Quantity
1	Laptop	50000	1
2	Phone	20000	2
1	Mouse	500	3
3	Laptop	50000	1
2	Mouse	500	1
4	Tablet	30000	1
3	Phone	20000	1
5	Laptop	50000	2"""

df = pd.read_csv(io.StringIO(data),sep="\s+")
print(df.head())
print(df.info())
print(df.describe())

df["Total"] = df["Price"] * df["Quantity"]
print(df.head())

Total_spending = df.groupby("CustomerID")["Total"].sum()
print(f"Total Spending {Total_spending}")

most_sold_product = df.groupby("Product")["Quantity"].sum().idxmax()
print(most_sold_product)

Top_2 = df.groupby("CustomerID")["Total"].sum().nlargest(2)
print(Top_2)

product_sales = df.groupby("Product")["Quantity"].sum()
product_sales.plot(kind="bar")
plt.show()