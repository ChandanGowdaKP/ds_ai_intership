import numpy as np


def main():
    # Step 1: Create 1D array from 0 to 23
    data = np.arange(24)

    print("Original 1D Array:")
    print(data)
    print("Shape:", data.shape)

    # Step 2: Reshape into (4, 3, 2)
    reshaped_data = data.reshape(4, 3, 2)

    print("\nReshaped to (4, 3, 2):")
    print(reshaped_data)
    print("Shape:", reshaped_data.shape)

    # Step 3: Transpose to (4, 2, 3)
    transposed_data = reshaped_data.transpose(0, 2, 1)

    print("\nTransposed to (4, 2, 3):")
    print(transposed_data)
    print("Final Shape:", transposed_data.shape)


if __name__ == "__main__":
    main()
