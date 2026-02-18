import pandas as pd
def main():
    # Create a Pandas Series with custom labels
    products = pd.Series(
        [700, 150, 300],
        index=["Laptop", "Mouse", "Keyboard"]
    )
    # Access price of 'Laptop' using label-based indexing
    laptop_price = products.loc["Laptop"]
    # Slice first two products using positional indexing
    first_two_products = products.iloc[:2]
    # Print results
    print("=== Full Product Price List ===")
    print(products)
    print("\n=== Price of Laptop ===")
    print(laptop_price)
    print("\n=== First Two Products (Positional Slice) ===")
    print(first_two_products)
if __name__ == "__main__":
    main()
