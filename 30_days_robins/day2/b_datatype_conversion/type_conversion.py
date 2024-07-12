"""Data Type Conversion
int(): Converts a value to an integer.
float(): Converts a value to a float.
str(): Converts a value to a string.
bool(): Converts a value to a boolean.
"""

# Type Conversion Basics

# 1. Converting to an Integer
# The int() function converts a value to an integer (whole number).

# Converting a string that represents a number to an integer
number_str = "42"
number_int = int(number_str)  # Convert the string "42" to the integer 42
print(f"The string '{number_str}' has been converted to the integer {number_int}.")

# Converting a float to an integer
number_float = 3.99
number_int_from_float = int(number_float)  # Convert the float 3.99 to the integer 3
print(f"The float {number_float} has been converted to the integer {number_int_from_float}.")

# 2. Converting to a Float
# The float() function converts a value to a float (decimal number).

# Converting a string that represents a decimal number to a float
decimal_str = "3.14"
decimal_float = float(decimal_str)  # Convert the string "3.14" to the float 3.14
print(f"The string '{decimal_str}' has been converted to the float {decimal_float}.")

# Converting an integer to a float
number_int = 7
number_float_from_int = float(number_int)  # Convert the integer 7 to the float 7.0
print(f"The integer {number_int} has been converted to the float {number_float_from_int}.")

# 3. Converting to a String
# The str() function converts a value to a string (text).

# Converting an integer to a string
number_int = 123
number_str = str(number_int)  # Convert the integer 123 to the string "123"
print(f"The integer {number_int} has been converted to the string '{number_str}'.")

# Converting a float to a string
decimal_float = 7.89
decimal_str = str(decimal_float)  # Convert the float 7.89 to the string "7.89"
print(f"The float {decimal_float} has been converted to the string '{decimal_str}'.")

# 4. Converting to a Boolean
# The bool() function converts a value to a boolean (True or False).

# Converting a non-empty string to a boolean
text = "Hello"
text_bool = bool(text)  # Convert the non-empty string "Hello" to True
print(f"The string '{text}' has been converted to the boolean {text_bool}.")

# Converting an empty string to a boolean
empty_text = ""
empty_text_bool = bool(empty_text)  # Convert the empty string "" to False
print(f"The empty string '' has been converted to the boolean {empty_text_bool}.")

# Converting a number to a boolean
number = 0
number_bool = bool(number)  # Convert the number 0 to False
print(f"The number {number} has been converted to the boolean {number_bool}.")

number = 5
number_bool = bool(number)  # Convert the number 5 to True
print(f"The number {number} has been converted to the boolean {number_bool}.")
