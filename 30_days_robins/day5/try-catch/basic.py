try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That's not a valid number!")

# In this example:

# The try block attempts to convert the input to an integer.
# If the input is not a valid integer,
# a ValueError is raised, and the code in the except block is executed.
