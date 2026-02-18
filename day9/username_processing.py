import pandas as pd
def main():
    # Step 1: Create the Series
    usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
    # Step 2: Remove whitespace and convert to lowercase
    cleaned_usernames = usernames.str.strip().str.lower()
    # Step 3: Check which usernames contain the letter 'a'
    contains_a = cleaned_usernames.str.contains('a')
    # Output results
    print("=== Cleaned Usernames ===")
    print(cleaned_usernames)

    print("\n=== Contains Letter 'a' ===")
    print(contains_a)

if __name__ == "__main__":
    main()
