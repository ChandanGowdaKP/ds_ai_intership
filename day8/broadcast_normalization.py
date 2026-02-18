import numpy as np
def main():
    # Step 1: Create a 5x3 array of random integers (50–100)
    np.random.seed(10)  # ensures same output every run
    scores = np.random.randint(50, 101, size=(5, 3))
    # Step 2: Calculate column-wise mean (axis=0)
    subject_means = scores.mean(axis=0)
    # Step 3: Subtract the mean using broadcasting
    centered_scores = scores - subject_means
    # Output results
    print("=== Original Scores (5 Students x 3 Subjects) ===")
    print(scores)
    print("\n=== Subject-wise Means ===")
    print(subject_means)
    print("\n=== Centered Scores (Scores - Subject Mean) ===")
    print(centered_scores)
if __name__ == "__main__":
    main()
