# Ask the user for their name
name = input("Enter your name: ")
# Ask the user for their current age
age = input("Enter your current age: ")
# Convert age to integer
age = int(age)
# Calculate age in 2030 (current year = 2026, so +4 years)
age_2030 = age + 4
# Print the result
print(f"Hey {name}, you will be {age_2030} years old in 2030!")
