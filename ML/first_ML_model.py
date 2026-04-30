from sklearn.datasets import fetch_california_housing
import pandas as pd
import numpy as np

data = fetch_california_housing()
df= pd.DataFrame(data.data,columns=data.feature_names)
print(df)

#prdedict price so added the target price columns

df["Price"]= data.target
df.head()
df.describe()
df.info()