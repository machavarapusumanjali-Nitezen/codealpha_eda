import pandas as pd

df = pd.read_csv("titanic.csv")

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSurvival Count:")
print(df["Survived"].value_counts())
"""import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

print("Dataset Shape:")
print(df.shape)

print("\nSurvival Count:")
print(df["Survived"].value_counts())

# Graph 1
df["Survived"].value_counts().plot(kind="bar")
plt.title("Survival Count")
plt.show()

# Graph 2
df["Sex"].value_counts().plot(kind="bar")
plt.title("Gender Distribution")
plt.show()

# Graph 3
df["Age"].hist(bins=20)
plt.title("Age Distribution")
plt.show()"""