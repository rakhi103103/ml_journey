import pandas as pd
import io

data = """Name      Age   Salary   City
Amit      25    50000    Mumbai
Sara      NaN   60000    Delhi
John      30    NaN      Mumbai
Amit      25    50000    Mumbai
Lisa      28    70000    NaN"""

df = pd.read_csv(io.StringIO(data), sep="\s+")


duplicate_drop = df.drop_duplicates(ignore_index=True)
print(duplicate_drop)

missing_age = df["Age"].mean(numeric_only=True)
df["Age"]=df["Age"].fillna(missing_age)
print(df["Age"])

missing_Salary = df["Salary"].median(numeric_only=True)
df["Salary"]=df["Salary"].fillna(missing_Salary)
print(df["Salary"])

df["City"] = df["City"].fillna("Unknown",inplace=True)
print(df["City"])

print(df.groupby("City")["Salary"].mean())

print(df[df["Salary"]>50000])

df["SalaryAfterTax"] = df["Salary"]*0.9
print(df["SalaryAfterTax"])
print(df)

