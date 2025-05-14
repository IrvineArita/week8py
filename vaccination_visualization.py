import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_covid_data.csv")

# Set style
sns.set(style="darkgrid")
plt.rcParams["figure.figsize"] = (12, 6)

# 1. Total Vaccinations Over Time

plt.figure()
for country in df["location"].unique():
    country_data = df[df["location"] == country]
    plt.plot(country_data["date"], country_data["total_vaccinations"], label=country)
plt.title("Cumulative COVID-19 Vaccinations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/total_vaccinations_over_time.png")
plt.show()

# 2. % Vaccinated Population (Latest Data)

# Assume % vaccinated = people_fully_vaccinated / population
# Merge with population column
latest_df = df.sort_values("date").groupby("location").tail(1)

# Filter only valid entries
latest_df = latest_df[latest_df["people_fully_vaccinated"] > 0]

# Calculate %
latest_df["vaccinated_pct"] = (latest_df["people_fully_vaccinated"] / latest_df["population"]) * 100

# Plot bar chart of vaccination %
plt.figure()
sns.barplot(x="location", y="vaccinated_pct", data=latest_df)
plt.title("Percentage of Fully Vaccinated Population by Country")
plt.ylabel("% Fully Vaccinated")
plt.xlabel("Country")
plt.tight_layout()
plt.savefig("outputs/vaccinated_percentage_bar.png")
plt.show()


# 3. Pie Chart : One Country

country = "United States"
us = latest_df[latest_df["location"] == country].iloc[0]

vaccinated = us["people_fully_vaccinated"]
unvaccinated = us["population"] - vaccinated

plt.figure()
plt.pie(
    [vaccinated, unvaccinated],
    labels=["Vaccinated", "Unvaccinated"],
    autopct="%1.1f%%",
    colors=["#4CAF50", "#FF5252"]
)
plt.title(f"Vaccination Breakdown – {country}")
plt.tight_layout()
plt.savefig("outputs/vaccination_pie_us.png")
plt.show()


country = "Kenya"
us = latest_df[latest_df["location"] == country].iloc[0]

vaccinated = us["people_fully_vaccinated"]
unvaccinated = us["population"] - vaccinated

plt.figure()
plt.pie(
    [vaccinated, unvaccinated],
    labels=["Vaccinated", "Unvaccinated"],
    autopct="%1.1f%%",
    colors=["#4CAF50", "#FF5252"]
)
plt.title(f"Vaccination Breakdown – {country}")
plt.tight_layout()
plt.savefig("outputs/vaccination_pie_us.png")
plt.show()


country = "India"
us = latest_df[latest_df["location"] == country].iloc[0]

vaccinated = us["people_fully_vaccinated"]
unvaccinated = us["population"] - vaccinated

plt.figure()
plt.pie(
    [vaccinated, unvaccinated],
    labels=["Vaccinated", "Unvaccinated"],
    autopct="%1.1f%%",
    colors=["#4CAF50", "#FF5252"]
)
plt.title(f"Vaccination Breakdown – {country}")
plt.tight_layout()
plt.savefig("outputs/vaccination_pie_us.png")
plt.show()
