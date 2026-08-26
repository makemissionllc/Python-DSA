# Question 6: Populate a list with 5 user inputs and calculate the average

# Initialize an empty list to store the values
values = []

# Use a loop to prompt the user for 5 numeric inputs
for i in range(5):
    num = float(input(f"Enter value {i + 1} of 5: "))
    values.append(num)  # Add the input value to the list

# Calculate the average by dividing the sum of values by the count of items
average = sum(values) / len(values)

# Display the entered values and the calculated average
print(f"\nValues entered: {values}")
print(f"Average of the values: {average:.2f}")