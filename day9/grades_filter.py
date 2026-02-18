import pandas as pd
def main():
    # Step 1: Create Series with missing values
    grades = pd.Series([85, None, 92, 45, None, 78, 55])
    # Step 2: Identify missing values
    missing_mask = grades.isnull()
    # Step 3: Fill missing values with 0
    filled_grades = grades.fillna(0)
    # Step 4: Filter scores greater than 60
    high_scores = filled_grades[filled_grades > 60]
    # Output results
    print("=== Original Grades ===")
    print(grades)
    print("\n=== Missing Value Mask ===")
    print(missing_mask)
    print("\n=== Grades After Filling Missing Values ===")
    print(filled_grades)
    print("\n=== Scores Greater Than 60 ===")
    print(high_scores)
if __name__ == "__main__":
    main()
