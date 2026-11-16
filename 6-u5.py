import pandas as pd

f = open("students.csv", "w")
f.write("Name,Age,Marks\n")
f.write("sushil,21,78\n")
f.write("Riya,22,85\n")
f.write("nikita,20,92\n")
f.close()

df = pd.read_csv("students.csv")
print("DataFrame from CSV:")
print(df)

data = [["Raj", 23, 67], ["Kiran", 21, 88]]
df2 = pd.DataFrame(data, columns=["Name", "Age", "Marks"])
print("\nDataFrame from list:")
print(df2)
