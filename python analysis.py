
---

# ✅ FINAL PYTHON CODE (FULL — COPY ALL)

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Preview data
print(df.head())

# -------------------------------
# DATA CLEANING
# -------------------------------
df.dropna(subset=["country", "date_added"], inplace=True)

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year

# -------------------------------
# 1. Movies vs TV Shows
# -------------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="type", data=df)
plt.title("Movies vs TV Shows on Netflix")
plt.savefig("chart1.png")
plt.show()

# -------------------------------
# 2. Content Added Over Years
# -------------------------------
plt.figure(figsize=(10,5))
df["year_added"].value_counts().sort_index().plot(kind="bar")
plt.title("Content Added Over Years")
plt.savefig("chart2.png")
plt.show()

# -------------------------------
# 3. Top 10 Countries
# -------------------------------
plt.figure(figsize=(10,5))
df["country"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Countries Producing Content")
plt.savefig("chart3.png")
plt.show()
