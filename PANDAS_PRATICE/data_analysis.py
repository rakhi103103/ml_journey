import pandas as pd
import io

data = """CustomerID   Product   Price   Quantity
1            Laptop    50000   1
2            Phone     20000   2
1            Mouse     500     3
3            Laptop    50000   1
2            Mouse     500     1"""

df = pd.read_csv(io.StringIO(data),sep="\s+")
# print(df)

df["Total"] = df["Price"] * df["Quantity"]
print(df)

Total_spend= df.groupby("CustomerID")["Total"].sum().reset_index(name="Total_Spent")
print(Total_spend)

most_sold = df.groupby("Product")["Quantity"].sum().idxmax()
ms = df["Product"].value_counts().head(1)
# most_sell = df.nlargest(3,"Product")
print(most_sold,ms)

top2 = df.assign(Total=df.Price*df.Quantity).groupby("CustomerID")["Total"].sum().nlargest(2)
print(top2)

print(df["CustomerID"].nunique())