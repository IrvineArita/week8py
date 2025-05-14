# analysis/data_loading_exploration.py

import pandas as pd

# Load the CSV file
df = pd.read_csv("owid-covid-data.csv")


# View the first 5 rows
print("📌 Preview of the dataset:")
print(df.head())

# View all column names
print("\n🧾 Column names in the dataset:")
print(df.columns)

# Check for missing values
print("\n🔍 Missing values in each column:")
print(df.isnull().sum())

# Check dataset shape (rows and columns)
print(f"\n📊 Dataset shape: {df.shape[0]} rows and {df.shape[1]} columns")

# Optional: View summary stats for numerical columns
print("\n📈 Summary statistics:")
print(df.describe())








