def cc(char):
    if char.isupper():
        return "uppercase"
    elif char.islower():
        return "lowercase"
    else:
        return "neither (it is not an alphabetic letter)"

usin = input("Enter a single character: ")

if len(usin) == 1:
    result = cc(usin)
    print(f"The character '{usin}' is {result}.")
else:
    print("Error: Please enter exactly one character.")