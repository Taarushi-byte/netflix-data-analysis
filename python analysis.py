
---

# 🟢 STEP 3: ADD THIS PYTHON FILE

👉 Create file: `analysis.py`  
👉 Paste FULL code:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset (we’ll replace with real later)
data = {
    "type": ["Movie", "TV Show", "Movie", "TV Show"],
    "release_year": [2020, 2019, 2021, 2018],
    "country": ["USA", "India", "UK", "USA"]
}

df = pd.DataFrame(data)

print(df.head())

# Count plot
sns.countplot(x="type", data=df)
plt.title("Movies vs TV Shows")
plt.show()

# Year distribution
df["release_year"].value_counts().sort_index().plot(kind="bar")
plt.title("Content Release Over Years")
plt.show()
