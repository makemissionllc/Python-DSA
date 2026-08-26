# Question 5: Python equivalent of the provided pseudocode loop

# Initialize variables x and y
x = 0
y = 20

# Implement REPEAT...UNTIL logic using a while loop
# The loop runs while y is NOT less than 6 (y >= 6)
while True:
    y -= 4  # SUBTRACT 4 FROM y
    x += 2 / y  # ADD 2/y TO x

    # UNTIL y IS LESS THAN 6 (exit condition)
    if y < 6:
        break

# DISPLAY x
print(f"The final value of x is: {x}")