import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
print(df)

#Highest score 
highest_score = df.max(numeric_only=True) 
print(f"Highest score: {highest_score}")

#average per subject
average_sub = df.iloc[:,1:-1].mean(axis=0)
print(f"\n\nAverage Score: {average_sub}")

#higest scorer
df["Total"] = df.iloc[:,1:].sum(axis=1)
higest_scorer = df.loc[df["Total"].idxmax()]
print(f"\nhighest scorer: {higest_scorer}") 

#lowest scorer
lowest_Scorer = df.loc[df["Total"].idxmin()]
print(f"\nLowest scorer: {lowest_Scorer}")


#how may passed
df["Average"] = df.iloc[:,1:-1].mean(axis=1)
passed_count = (df["Average"]>=50).sum()
print(f"Passed count: {passed_count}")

#Average per students
scores = df.iloc[:,1:].to_numpy()
avg= np.mean(scores,axis = 1)

df["Average"]=avg
print(df[["Name","Average"]])

#bar graph
plt.figure()
plt.bar(average_sub.index,average_sub.values)
#labels
plt.xlabel("Subjects")
plt.ylabel("Averge Score")
plt.title("Averge Score per subject")
plt.show()