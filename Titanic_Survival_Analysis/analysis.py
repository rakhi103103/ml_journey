import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# step 1:  Load the dataset

df=pd.read_csv("Titanic-Dataset.csv")

print(df.head())
print(f"\n\nShapes: {df.shape}")
print(f"\n\nColumns: {df.columns.tolist()}")
print(f"\n\nData_Type\n: {df.dtypes}")

# step 2:Find out exactly which columns have missing values and how many. 
# Also calculate the missing percentage for each column.

missing_value = df.isnull().sum()
missing_percentage =(missing_value / len(df)) *100
print(f"\n\nMissing Value: {missing_value}")
print(f"\n\nmissing percentage for each column: {missing_percentage} ")

# step 3: Fill missing Age with median. Fill missing Embarked with mode. Drop the Cabin column entirely.

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])
df = df.drop(columns =["Cabin"])

print(f"\n\nAfter cleaning the missing value: {df.isnull().sum()}")

#  SECTION 2 — NumPy Operations (this is what impresses recruiters)

# step 4: Using NumPy, calculate mean, median, std, min, max of the Age column. 
# Also find the 25th, 50th, and 75th percentile of Fare.

age = df["Age"].to_numpy()
mean = np.mean(age)
median = np.median(age)
std = np.std(age)
min = np.min(age)
max = np.max(age)

fare = df["Fare"].to_numpy()
p25,p50,p75 = np.percentile(fare,[25,50,75])
print(f"\n\nMean= {mean:.2f},\nMedian= {median:.2f},\nstd= {std:.2f},\n Min= {min:.2f},\nMax= {max:.2f}")
print(f"\n\n25th = {p25:.2f}")
print(f"\n50th = {p50:.2f}")
print(f"\n75th = {p75:.2f}\n\n")

# STEP 5:  Using np.where, create a new column
#  AgeGroup — "Child" if Age < 18, "Adult" if 18–60, "Senior" if above 60.

df["AgeGroup"] = np.where(df["Age"]<18,"Child",np.where(df["Age"]>=60,"Senior","Adult"))
value_counts = df["AgeGroup"].value_counts()

print(df["AgeGroup"])
print(f"\n\nvalues counts of age groups: {value_counts}")

#step 6: Using np.select,
# create a FareCategory column — "Low" (Fare < 10), "Medium" (10–50), "High" (above 50).
conditions=[
    df["Fare"]<10,
    df["Fare"]<=50
]
choices=["low","Medium"]

df["FareCategory"]=np.select(conditions,choices,default="High")
print(df["FareCategory"])

#step 7: . Using NumPy boolean masking, find all passengers who paid above the 90th percentile fare.
#  How many are there and what % survived?
p90 = np.percentile(df["Fare"],90)
print(f"The 90% fare threshold = {p90}")
mask = df["Fare"]>p90
print(f"\n\nmask: {mask}")

how_many = mask.sum()
print(f"\nthe passenger above 90 =  {how_many}")

Survied = df.loc[mask,"Survived"].mean()*100
print(f'\nThe % of passenger survived = {Survied}')

# step 8:  Find survival rate by Sex, by Pclass, and by Embarked. Sort each result descending.

gender_survived = df.groupby("Sex")["Survived"].mean().sort_values(ascending=False)
Pclass_survived = df.groupby("Pclass")["Survived"].mean().sort_values(ascending=False)
Embarked_survived = df.groupby("Embarked")["Survived"].mean().sort_values(ascending=False)
print(f"\n\nsurvival rate by genders : {gender_survived} \n survival rate by Pclass: {Pclass_survived}")
print(f"survival rate by Embarked: {Embarked_survived}")

# step 9:  Using transform, add a column AvgFareByClass — the average fare of each passenger's class
#  (so every passenger in class 1 gets the same average value).
df["AvgFareByClass"]=df.groupby("Pclass")["Fare"].transform("mean")
head5 = df.loc[:,["Pclass","Fare","AvgFareByClass"]].head()
print(head5)

# step 10 :  Create a crosstab of Sex vs Survived.
#  Then create a pivot table showing average Fare by Pclass and Sex.
crosst = pd.crosstab(df["Sex"],df["Survived"])
print(f"\n\ncrosstab of Sex vs Survived: {crosst}")

pivot = pd.pivot_table(
    df,
    index="Pclass",
    columns="Sex",
    values="Fare",
    aggfunc=np.mean
).round(2)

print(f"\n\npivot table showing average Fare by Pclass and Sex: {pivot}")

# step 11: Find the top 5 passengers who paid the highest fare.
#  Show only Name, Pclass, Fare, Survived.
top5 = df.nlargest(5, "Fare")[["Name","Pclass","Fare","Survived"]]
print(top5)

# step 12 : Bar chart — Survival count (Survived vs Died) with proper labels and colors.
Survival_counts = df["Survived"].value_counts()
plt.bar(["Died","Survived"],Survival_counts.values,color=["red","green"])
plt.title("Survival Count on Titanic")
plt.xlabel("Outcome")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("survival_count.png")
plt.show()

# step 13: Grouped bar chart — survival rate by Pclass and Sex together.
survival_grouped = df.groupby(["Pclass", "Sex"])["Survived"].mean().unstack()

x = np.arange(len(survival_grouped.index))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(x - width/2, survival_grouped["female"], width, label="Female", color="#e91e8c")
ax.bar(x + width/2, survival_grouped["male"], width, label="Male", color="#1e90ff")

ax.set_xticks(x)
ax.set_xticklabels(["Class 1", "Class 2", "Class 3"])
ax.set_title("Survival Rate by Class and Gender")
ax.set_ylabel("Survival Rate")
ax.legend()
plt.tight_layout()
plt.savefig("survival_by_class_gender.png")
plt.show()


# step 14. Histogram — Age distribution of survivors vs non-survivors overlaid.
survived = df[df["Survived"] == 1]["Age"]
died = df[df["Survived"] == 0]["Age"]

plt.figure(figsize=(8, 5))
plt.hist(died.to_numpy(), bins=30, alpha=0.6, color="#e74c3c", label="Died")
plt.hist(survived.to_numpy(), bins=30, alpha=0.6, color="#2ecc71", label="Survived")
plt.title("Age Distribution: Survivors vs Non-Survivors")
plt.xlabel("Age")
plt.ylabel("Count")
plt.legend()
plt.tight_layout()
plt.savefig("age_distribution.png")
plt.show()


# step 15. Pie chart — breakdown of passengers by AgeGroup (Child / Adult / Senior).

age_group_counts = df["AgeGroup"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    age_group_counts.values,
    labels=age_group_counts.index,
    autopct="%1.1f%%",
    colors=["#3498db", "#f39c12", "#9b59b6"],
    startangle=140
)
plt.title("Passenger Age Group Distribution")
plt.tight_layout()
plt.savefig("age_group_pie.png")
plt.show()



# step 16. Print a clean final summary of key findings.

female_survival = df[df["Sex"] == "female"]["Survived"].mean() * 100
male_survival = df[df["Sex"] == "male"]["Survived"].mean() * 100
class1_survival = df[df["Pclass"] == 1]["Survived"].mean() * 100
class3_survival = df[df["Pclass"] == 3]["Survived"].mean() * 100
child_survival = df[df["AgeGroup"] == "Child"]["Survived"].mean() * 100

print("=" * 45)
print("       TITANIC — KEY INSIGHTS")
print("=" * 45)
print(f"Female survival rate      : {female_survival:.1f}%")
print(f"Male survival rate        : {male_survival:.1f}%")
print(f"1st class survival rate   : {class1_survival:.1f}%")
print(f"3rd class survival rate   : {class3_survival:.1f}%")
print(f"Children survival rate    : {child_survival:.1f}%")
print("=" * 45)