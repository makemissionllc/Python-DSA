# Question 2: Calculate the volume of a sphere given its radius

# Import the math module to get an precise value for pi
import math

# Ask the user for the radius of the sphere and convert it to a float
radius = float(input("Enter the radius of the sphere: "))

# Calculate the volume using the formula (4/3) * pi * (r**3)
# Using the Python exponent operator ** to compute r cubed
volume = (4 / 3) * math.pi * (radius**3)

# Display the calculated volume rounded to 2 decimal places
print(f"The volume of a sphere with radius {radius} is: {volume:.2f}")