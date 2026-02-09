def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


# Taking user input
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# Function call
area, perimeter = calc_rectangle(length, width)

# Output
print(f"Area: {area}, Perimeter: {perimeter}")
