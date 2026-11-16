import pandas as pd
import numpy as np

data = {
    "Name":  ["Amit", "Riya", "Neha", "Raj"],
    "Age":   [21, np.nan, 20, 23],
    "Marks": [78, 85, np.nan, np.nan]
}
df = pd.DataFrame(data)

print("Original data:\n", df)
print("\nMissing values in each column:\n", df.isnull().sum())

print("\nAfter dropna():\n", df.dropna())
print("\nAfter fillna(0):\n", df.fillna(0))

df["Age"] = df["Age"].fillna(df["Age"].mean())
print("\nAge filled with mean value:\n", df)
