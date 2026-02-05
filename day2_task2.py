# Ask for the total bill amount (float)
total_bill = float(input("Enter the total bill amount: "))
# Ask for number of people (int)
people = int(input("Enter the number of people: "))
# Calculate share per person
share_per_person = total_bill / people
# Output result
print(f"Total Bill: {total_bill}. Each person pays: {share_per_person}")
# Bonus: verify data types
print(type(total_bill))
print(type(people))
print(type(share_per_person))
