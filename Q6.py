val = []

for i in range(5):
    num = input(f"Enter value {i + 1} of 5: ")
    num = float(num)
    val.append(num)

ave = sum(val) / len(val)

# Display the entered values and the calculated average
print(f"\nValues entered: {val}")
print(f"Average of the values: {ave}")