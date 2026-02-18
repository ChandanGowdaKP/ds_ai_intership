# -----------------------------
# 1. Import Libraries
# -----------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# -----------------------------
# 2. Load Dataset
# -----------------------------
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# -----------------------------
# 3. Scatter Plot
#    AveRooms vs MedHouseVal
# -----------------------------
plt.figure()
plt.scatter(df['AveRooms'], df['MedHouseVal'])
plt.xlabel("Average Number of Rooms (House Size Proxy)")
plt.ylabel("Median House Value")
plt.title("House Size vs Price")
plt.show()

# -----------------------------
# 4. Create Categorical Variable
# -----------------------------
df['Income_Level'] = pd.cut(
    df['MedInc'],
    bins=3,
    labels=["Low Income", "Medium Income", "High Income"]
)

# -----------------------------
# 5. Boxplot
#    Income Level vs House Price
# -----------------------------
plt.figure()
df.boxplot(column='MedHouseVal', by='Income_Level')
plt.title("House Price Distribution by Income Level")
plt.suptitle("")  # removes automatic subtitle
plt.xlabel("Income Level")
plt.ylabel("Median House Value")
plt.show()
