import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("cdall.csv")

# Count city occurrences
city_counts = df["city"].value_counts()

# Get the top 50 cities
top_50_cities = city_counts.head(50)

# Plot
plt.figure(figsize=(30, 6))
top_50_cities.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Top 50 Cities by Number of Appearances", fontsize=14)
plt.xlabel("City", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()