# analysis/data_cleaning.py

import pandas as pd

# Load the raw dataset
df = pd.read_csv("owid-covid-data.csv")

# ✅ Add more countries of interest
countries = ["Kenya", "United States", "India", "Australia", "Japan"]
df = df[df["location"].isin(countries)]

# Drop rows where date is missing
df = df.dropna(subset=["date"])

# Convert 'date' column to datetime format
df["date"] = pd.to_datetime(df["date"])

# Handle missing values for key numeric columns
numeric_cols = [
    "total_cases", "new_cases", "total_deaths", "new_deaths",
    "total_vaccinations", "people_fully_vaccinated"
]

# Forward fill missing values
df[numeric_cols] = df[numeric_cols].fillna(method="ffill")

# Fill remaining missing values with 0
df[numeric_cols] = df[numeric_cols].fillna(0)

# Reset index
df = df.reset_index(drop=True)

# Save the cleaned dataset
df.to_csv("cleaned_covid_data.csv", index=False)

print("✅ Data cleaning complete. Cleaned data saved to 'data/cleaned_covid_data.csv'")
