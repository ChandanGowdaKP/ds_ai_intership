import pandas as pd

# Read Excel file
df = pd.read_excel("students.xlsx")

# Print entire file
print(df)

print("\nStudents who Passed:")
# Filter and print only passed students
passed_students = df[df["Status"] == "Pass"]
print(passed_students["Name"])
