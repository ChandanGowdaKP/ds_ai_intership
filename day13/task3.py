# -----------------------------
# 1. Import Libraries
# -----------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing

# -----------------------------
# 2. Load Dataset
# -----------------------------
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# -----------------------------
# 3. Correlation Matrix
# -----------------------------
corr_matrix = df.corr()

plt.figure()
sns.heatmap(corr_matrix, annot=False)
plt.title("Correlation Matrix Heatmap")
plt.show()

# -----------------------------
# 4. Find Highly Correlated Pairs (> 0.8)
# -----------------------------
high_corr = []

for i in range(len(corr_matrix.columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > 0.8:
            high_corr.append(
                (corr_matrix.columns[i],
                 corr_matrix.columns[j],
                 corr_matrix.iloc[i, j])
            )

print("Highly Correlated Pairs (>0.8):")
for pair in high_corr:
    print(pair)

# -----------------------------
# 5. Boxplot for Outliers
# -----------------------------
plt.figure()
sns.boxplot(y=df['MedHouseVal'])
plt.title("Boxplot of Median House Value")
plt.show()
