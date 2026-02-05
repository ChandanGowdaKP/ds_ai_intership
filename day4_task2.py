# Raw list with duplicate user IDs
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

# Convert the list into a set to keep only unique IDs
unique_users = set(raw_logs)

# Membership test to check if a specific ID exists
is_id05_present = "ID05" in unique_users

# Compare counts to show how duplicates are removed
original_count = len(raw_logs)
unique_count = len(unique_users)

# Output results
print("Unique User IDs:", unique_users)
print("Is ID05 present?", is_id05_present)
print("Original log count:", original_count)
print("Unique user count:", unique_count)
