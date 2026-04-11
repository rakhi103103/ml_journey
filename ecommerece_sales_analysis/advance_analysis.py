import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io

data = """CustomerID	Product	Category	Price	Quantity
1	Laptop	Electronics	50000	1
2	Phone	Electronics	20000	2
1	Mouse	Accessories	500	3
3	Laptop	Electronics	50000	1
2	Mouse	Accessories	500	1
4	Tablet	Electronics	30000	1
3	Phone	Electronics	20000	1
5	Laptop	Electronics	50000	2
4	Keyboard	Accessories	1500	2
2	Tablet	Electronics	30000	1"""

df= pd.read_csv(io.StringIO(data),sep="\s+")
print(df.head())

df["Total"] = df["Price"] * df["Quantity"]
df["DiscountedPrice"] = df["Total"] * 0.9

# print(df.head())

df["CutomerType"] = np.where(df["Total"] <2000 ,"Low",np.where(df["Total"]<=30000,"Medium","High"))
print(df)

Total_revnue = df.groupby("Product")["Total"].sum().sort_values(ascending=False)
print(Total_revnue)

Category_revenue = df.groupby("Category")["Total"].sum()
print(Category_revenue)

pivot = pd.pivot_table(
    df,
    values="Quantity",
    index="Product",
    columns="CustomerID",
    aggfunc="sum",
    fill_value=0
)

pivot["TotalSales"] = pivot.sum(axis =1)
pivot = pivot.sort_values("TotalSales",ascending=False)

print(pivot)

#numpy function

Average_price = np.mean(df["Price"])
max_price = np.max(df["Price"])
min_price = np.min(df["Price"])
standard_dev = np.std(df["Price"])

print(f"Average_price: {Average_price},max_price: {max_price},min_price: {min_price},standard_dev: {standard_dev}")

#highest Revenue
higest_val_transc = df[df["Total"]>40000]
print(higest_val_transc)

#Total revnue
plt.figure(figsize=(8,5))
Total_revnue.plot(kind="bar")
plt.title("Total revnue")
plt.xlabel("Product")
plt.ylabel("Total")
plt.show()

#Category revnue
plt.figure(figsize=(8,5))
Category_revenue.plot(kind="bar")
plt.title("Category Revnue")
plt.xlabel("Category")
plt.ylabel("Total")
plt.show()

#customer Spending
Customer_spending = df.groupby("CustomerID")["Total"].sum()
plt.figure(figsize=(8,5))
Customer_spending.plot(kind="bar")
plt.title("Customer Spemding")
plt.xlabel("CustomerID")
plt.ylabel("Total Spending")
plt.show()

#-----final insight------------

top_product = df.groupby("Product")["Total"].sum().idxmax()
highest_reven_cat = df.groupby("Category")["Total"].sum().idxmax()
top_customer = df.groupby("CustomerID")["Total"].sum().idxmax()
highest_transc = df["Total"].max()

print("\n\n ----------------BUSINESS INSIGHT------------------")
print(f"\n\nTop Product by revnue: {top_product}")
print(f"\nHighest revnue by category: {highest_reven_cat}")
print(f"\nTop Customer: {top_customer}")
print(f"\nHighest Transcation: {highest_transc}\n\n")