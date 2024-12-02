import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("Cities_and_Dates1.csv")

# Count city occurrences
city_counts = df["city"].value_counts()

# Plot
plt.figure(figsize=(10, 6))
city_counts.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Number of Appearances per City", fontsize=14)
plt.xlabel("City", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()


