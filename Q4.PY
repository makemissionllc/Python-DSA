# Question 4: Check if a given character is uppercase or lowercase using functions


def check_case(char):
    """Determines if a given character is uppercase, lowercase, or non-alphabetic."""
    if char.isupper():
        return "uppercase"
    elif char.islower():
        return "lowercase"
    else:
        return "neither (it is not an alphabetic letter)"


# Main program flow
# Ask the user to enter a single character
user_input = input("Enter a single character: ")

# Check if the user entered exactly one character
if len(user_input) == 1:
    result = check_case(user_input)
    print(f"The character '{user_input}' is {result}.")
else:
    print("Error: Please enter exactly one character.")