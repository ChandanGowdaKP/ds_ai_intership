# =========================
# Import Required Libraries
# =========================
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# =========================
# Step 1: Create Dataset (20 rows)
# =========================
df = pd.DataFrame({
    "Transmission": [
        "Automatic", "Manual", "Manual", "Automatic", "Manual",
        "Automatic", "Manual", "Automatic", "Manual", "Automatic",
        "Manual", "Automatic", "Manual", "Automatic", "Manual",
        "Automatic", "Manual", "Automatic", "Manual", "Automatic"
    ],
    "Color": [
        "Red", "Blue", "Green", "Red", "Blue",
        "Green", "Red", "Blue", "Green", "Red",
        "Blue", "Green", "Red", "Blue", "Green",
        "Red", "Blue", "Green", "Red", "Blue"
    ]
})

print("Original Dataset:\n")
print(df)

# =========================
# Step 2: Label Encoding (Transmission)
# =========================
le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])

print("\nAfter Label Encoding:\n")
print(df)

# =========================
# Step 3: One-Hot Encoding (Color)
# drop_first=True avoids Dummy Variable Trap
# =========================
df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print("\nFinal Encoded Dataset:\n")
print(df)

print("\nShape of dataset:", df.shape)
