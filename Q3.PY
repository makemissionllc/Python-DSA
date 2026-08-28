def calculate_area(side):
    return side*side


def calculate_perimeter(side):
    return  side*4

sidlen = input("Enter the side length of the square: ")
sidlen = float(sidlen)

area = calculate_area(sidlen)
perimeter = calculate_perimeter(sidlen)

print(f"For a square with side length {sidlen}:")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

