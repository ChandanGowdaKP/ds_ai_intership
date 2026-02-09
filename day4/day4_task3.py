# Create sets representing interests of two friends
friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

# Find common interests (intersection)
shared_interests = friend_a & friend_b

# Find all unique interests (union)
all_interests = friend_a | friend_b

# Find interests unique to friend_a (difference)
unique_to_a = friend_a - friend_b

# Output results
print("Shared Interests:", shared_interests)
print("All Interests:", all_interests)
print("Interests Unique to Friend A:", unique_to_a)
