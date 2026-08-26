# Question 3: Calculate the area and perimeter of a square using functions


def calculate_area(side):
    """Calculates and returns the area of a square."""
    return side**2


def calculate_perimeter(side):
    """Calculates and returns the perimeter of a square."""
    return 4 * side


# Main program flow
# Prompt the user to enter the side length of the square
side_length = float(input("Enter the side length of the square: "))

# Call the functions to compute area and perimeter
area = calculate_area(side_length)
perimeter = calculate_perimeter(side_length)

# Display the calculated values to the user
print(f"For a square with side length {side_length}:")
print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")