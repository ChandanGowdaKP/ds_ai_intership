# 1. Create a dictionary to store contact names as keys and phone numbers as values
contacts = {
    "Amit": "9876543210",
    "Sneha": "9123456780",
    "Rahul": "9988776655"
}
# 2. Add a new contact to the dictionary
contacts["Priya"] = "9012345678"
# 3. Update the phone number of an existing contact
contacts["Amit"] = "9000000000"
# 4. Safely retrieve an existing contact using .get()
existing_contact = contacts.get("Sneha", "Contact not found")
# 5. Safely retrieve a non-existent contact using .get() with a default message
missing_contact = contacts.get("Vikram", "Contact not found")
# 6. Print the results of safe lookups
print("Lookup Results:")
print("Sneha:", existing_contact)
print("Vikram:", missing_contact)
# 7. Iterate through the dictionary using .items()
print("\nContact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
# 8. Final output shows updated, added, and safely accessed contact data
