import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("cleaned_covid_data.csv")

# Set plot style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)


# 1. Total Cases Over Time

plt.figure()
for country in df["location"].unique():
    country_data = df[df["location"] == country]
    plt.plot(country_data["date"], country_data["total_cases"], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/total_cases_over_time.png")
plt.show()


# 2. Total Deaths Over Time

plt.figure()
for country in df["location"].unique():
    country_data = df[df["location"] == country]
    plt.plot(country_data["date"], country_data["total_deaths"], label=country)
plt.title("Total COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/total_deaths_over_time.png")
plt.show()


# 3. New Cases Per Day
plt.figure()
for country in df["location"].unique():
    country_data = df[df["location"] == country]
    plt.plot(country_data["date"], country_data["new_cases"], label=country)
plt.title("Daily New COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/daily_new_cases.png")
plt.show()


# 4. Death Rate Over Time

df["death_rate"] = df["total_deaths"] / df["total_cases"]
df["death_rate"] = df["death_rate"].fillna(0)

plt.figure()
for country in df["location"].unique():
    country_data = df[df["location"] == country]
    plt.plot(country_data["date"], country_data["death_rate"], label=country)
plt.title("COVID-19 Death Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Death Rate")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/death_rate_over_time.png")
plt.show()
