# ============================================
# Feature Scaling Demonstration (VS Code Ready)
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def main():

    # ---------------------------------
    # Step 1: Create Sample Dataset
    # ---------------------------------
    np.random.seed(42)

    data = pd.DataFrame({
        "Age": np.random.randint(20, 60, 200),
        "Salary": np.random.randint(20000, 120000, 200)
    })

    print("\n===== ORIGINAL DATA (First 5 Rows) =====\n")
    print(data.head())

    # ---------------------------------
    # Step 2: Standardization
    # (Mean = 0, Std = 1)
    # ---------------------------------
    standard_scaler = StandardScaler()
    data_standardized = pd.DataFrame(
        standard_scaler.fit_transform(data),
        columns=data.columns
    )

    print("\n===== STANDARDIZED DATA (First 5 Rows) =====\n")
    print(data_standardized.head())

    # ---------------------------------
    # Step 3: Normalization
    # (Range 0 to 1)
    # ---------------------------------
    minmax_scaler = MinMaxScaler()
    data_normalized = pd.DataFrame(
        minmax_scaler.fit_transform(data),
        columns=data.columns
    )

    print("\n===== NORMALIZED DATA (First 5 Rows) =====\n")
    print(data_normalized.head())

    # ---------------------------------
    # Step 4: Plot Histograms
    # ---------------------------------

    # Original Salary Distribution
    plt.figure()
    plt.hist(data["Salary"], bins=20)
    plt.title("Original Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Frequency")
    plt.show()

    # Standardized Salary Distribution
    plt.figure()
    plt.hist(data_standardized["Salary"], bins=20)
    plt.title("Standardized Salary Distribution (Mean=0, Std=1)")
    plt.xlabel("Standardized Salary")
    plt.ylabel("Frequency")
    plt.show()

    # Normalized Salary Distribution
    plt.figure()
    plt.hist(data_normalized["Salary"], bins=20)
    plt.title("Normalized Salary Distribution (0 to 1)")
    plt.xlabel("Normalized Salary")
    plt.ylabel("Frequency")
    plt.show()

    # ---------------------------------
    # Summary Statistics
    # ---------------------------------
    print("\n===== SUMMARY =====\n")
    print("Original Salary Mean:", data["Salary"].mean())
    print("Original Salary Std:", data["Salary"].std())

    print("\nStandardized Salary Mean:", data_standardized["Salary"].mean())
    print("Standardized Salary Std:", data_standardized["Salary"].std())

    print("\nNormalized Salary Min:", data_normalized["Salary"].min())
    print("Normalized Salary Max:", data_normalized["Salary"].max())


# Run the program
if __name__ == "__main__":
    main()
