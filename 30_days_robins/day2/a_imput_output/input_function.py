# The input() Function
# The input() function is used to read a string of text from the user via the console.

# Basic Usage
# Prompt the user to enter their name
name = input("Please enter your name: ")
# The text inside the parentheses ("Please enter your name: ") is displayed to the user as a prompt.
# The user types their name and presses Enter. The input() function captures this input and stores it in the variable 'name'.
print(f"Hello, {name}!")  # Outputs a greeting using the name provided by the user.

# Converting User Input
# By default, input() captures the input as a string. To use the input as a number, we need to convert it.
age = input("Please enter your age: ")
# The user enters their age, for example, "25".
# We need to convert this string to an integer for numerical operations.
age = int(age)
print(f"You are {age} years old.")  # Outputs the user's age.

# Handling Multiple Inputs
# We can ask the user for multiple pieces of information and use them together.
first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

# Convert the inputs to integers
first_number = int(first_number)
second_number = int(second_number)

# Calculate the sum of the two numbers
sum_result = first_number + second_number

# Display the result
print(f"The sum of {first_number} and {second_number} is {sum_result}.")


# NB: DO NOT learn  anything below 👇: you may not understand if you are a beginner
# you can refer later
# Using input() in a Loop
# We can use input() inside a loop to repeatedly ask the user for input.
# For example, a simple number guessing game:
correct_number = 7
guess = None

while guess != correct_number:
    guess = int(input("Guess the number (between 1 and 10): "))
    if guess < correct_number:
        print("Too low, try again!")
    elif guess > correct_number:
        print("Too high, try again!")

print("Congratulations! You guessed the correct number.")

# Validating User Input
# Sometimes, we need to make sure the user provides valid input. We can use a loop to keep asking until the input is valid.
while True:
    try:
        height = float(input("Please enter your height in meters (e.g., 1.75): "))
        break  # Exit the loop if the input is valid
    except ValueError:
        print("That's not a valid number. Please try again.")

print(f"Your height is {height} meters.")

# Using input() with Default Values
# Although input() does not directly support default values, we can achieve this by providing a suggestion in the prompt and handling an empty input.
default_name = "Guest"
user_input = input(f"Enter your name (default is {default_name}): ")
name = user_input if user_input else default_name

print(f"Hello, {name}!")  # Greets the user, using "Guest" if no name was entered.

# Summary of input() Usage
# 1. Basic input capture and storage in a variable.
# 2. Converting input to different data types (e.g., int, float).
# 3. Handling multiple inputs for calculations or operations.
# 4. Using input() in loops for repeated input capture.
# 5. Validating input to ensure it meets certain criteria.
# 6. Providing default values when the user doesn't enter any input.

#'''' All these use cases help make programs interactive and user-friendly,
# allowing for dynamic input and responses based on user actions.
''''''