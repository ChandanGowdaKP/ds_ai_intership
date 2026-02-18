# -----------------------------
# 1. Import Libraries
# -----------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_california_housing

# -----------------------------
# 2. Load Built-in Dataset
# -----------------------------
housing = fetch_california_housing(as_frame=True)
df = housing.frame

print("First 5 Rows:")
print(df.head())

# -----------------------------
# 3. Pick Numerical Column
#    (MedHouseVal = Median House Value)
# -----------------------------
price = df['MedHouseVal']

# -----------------------------
# 4. Histogram with KDE
# -----------------------------
plt.figure()
sns.histplot(price, kde=True)
plt.title("Distribution of Median House Value")
plt.xlabel("Median House Value")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# 5. Skewness and Kurtosis
# -----------------------------
skewness = price.skew()
kurtosis = price.kurt()

print("\nSkewness:", skewness)
print("Kurtosis:", kurtosis)

# -----------------------------
# 6. Create a Categorical Column
#    (Since dataset has no categorical feature)
#    We'll create one based on Income Level
# -----------------------------
df['Income_Level'] = pd.cut(
    df['MedInc'],
    bins=3,
    labels=["Low Income", "Medium Income", "High Income"]
)

# -----------------------------
# 7. Count Plot for Categorical Variable
# -----------------------------
plt.figure()
sns.countplot(x='Income_Level', data=df)
plt.title("Count of Houses by Income Level")
plt.show()
