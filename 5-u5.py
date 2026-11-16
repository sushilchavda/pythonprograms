import pandas as pd

data = {
    "Name":   ["sushil", "Riya", "Nikita", "avesh", "Kiran"],
    "Age":    [21, 22, 20, 23, 21],
    "Marks":  [78, 85, 92, 67, 88]
}
df = pd.DataFrame(data)

print(df)
print("\nFirst 2 rows:\n", df.head(2))
print("\nLast 2 rows:\n", df.tail(2))
print("\nShape   :", df.shape)
print("Columns :", list(df.columns))
print("Size    :", df.size)
print("\nData types:\n", df.dtypes)
print("\nDescription:\n", df.describe())
print("\nMaximum marks:", df["Marks"].max())
print("Minimum marks:", df["Marks"].min())
print("Average marks:", df["Marks"].mean())

print("\nSorted by Marks:\n", df.sort_values("Marks", ascending=False))
print("\nRow with index 2:\n", df.loc[2])
