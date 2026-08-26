# Question 1: Convert number of days to seconds

# Prompt the user to enter the number of days and convert the input to a float
days = float(input("Enter the number of days: "))

# Calculate total seconds: 1 day = 24 hours * 60 minutes * 60 seconds = 86,400 seconds
seconds = days * 24 * 60 * 60

# Display the resulting number of seconds
print(f"There are {seconds:,.2f} seconds in {days} day(s).")
