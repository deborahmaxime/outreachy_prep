import pandas as pd

# 1. Load the dataset from GitHub
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 2. Data Overview
print("Data Overview:")
print(df.head())

# 3. Base Information
print("\nNumber of Passengers :", len(df))
print("Columns :", list(df.columns))

# 4. Simple Statistics
print("\nAverage Age :", df["Age"].mean())
print("Overall Survival Rate :", df["Survived"].mean())

# 5. Small Grouping : Survival by Sex
print("\nSurvival Rate by Sex :")
print(df.groupby("Sex")["Survived"].mean())