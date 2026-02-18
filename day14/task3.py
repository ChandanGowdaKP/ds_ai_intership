# =====================================================
# Polynomial Features vs Linear Regression (VS Ready)
# =====================================================

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def main():

    # -------------------------------------
    # Step 1: Create Non-Linear Dataset
    # y = 3x^2 + 2x + noise
    # -------------------------------------
    np.random.seed(42)

    X = np.linspace(-10, 10, 200).reshape(-1, 1)
    y = 3 * X**2 + 2 * X + np.random.normal(0, 20, size=X.shape)

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # -------------------------------------
    # Model 1: Simple Linear Regression
    # -------------------------------------
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)

    y_pred_linear = linear_model.predict(X_test)
    r2_linear = r2_score(y_test, y_pred_linear)

    # -------------------------------------
    # Model 2: Polynomial Regression (Degree=2)
    # -------------------------------------
    poly = PolynomialFeatures(degree=2)

    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)

    poly_model = LinearRegression()
    poly_model.fit(X_train_poly, y_train)

    y_pred_poly = poly_model.predict(X_test_poly)
    r2_poly = r2_score(y_test, y_pred_poly)

    # -------------------------------------
    # Print Results
    # -------------------------------------
    print("\n===== R² Comparison =====")
    print("Linear Regression R² Score:", r2_linear)
    print("Polynomial Regression (Degree=2) R² Score:", r2_poly)

    # -------------------------------------
    # Plot Results
    # -------------------------------------
    X_plot = np.linspace(-10, 10, 200).reshape(-1, 1)

    # Linear prediction
    y_plot_linear = linear_model.predict(X_plot)

    # Polynomial prediction
    X_plot_poly = poly.transform(X_plot)
    y_plot_poly = poly_model.predict(X_plot_poly)

    plt.figure()
    plt.scatter(X, y)
    plt.plot(X_plot, y_plot_linear)
    plt.plot(X_plot, y_plot_poly)
    plt.title("Linear vs Polynomial Regression")
    plt.xlabel("X")
    plt.ylabel("y")
    plt.show()


if __name__ == "__main__":
    main()
