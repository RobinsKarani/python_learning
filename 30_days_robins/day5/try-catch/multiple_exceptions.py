try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"The result is: {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You cannot divide by zero!")

# In this example:

'''The try block attempts to convert the input to an integer and 
then divide 10 by that number.
If a ValueError occurs, it means the input was not 
a valid number.
If a ZeroDivisionError occurs, it means the user tried to divide by zero.'''