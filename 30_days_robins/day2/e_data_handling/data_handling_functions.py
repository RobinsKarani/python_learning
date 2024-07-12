# NOT FOR BEGINNERS
# Basic Data Handling in Python

# 1. Using type()
# The type() function returns the type of object. This is useful to check what kind of data you're working with.

# Example with an integer
number = 10
print(f"The type of {number} is {type(number)}.")  # Outputs: <class 'int'>

# Example with a string
text = "Hello, world!"
print(f"The type of '{text}' is {type(text)}.")  # Outputs: <class 'str'>

# Example with a list
numbers_list = [1, 2, 3, 4, 5]
print(f"The type of {numbers_list} is {type(numbers_list)}.")  # Outputs: <class 'list'>

# Example with a tuple
coordinates = (10, 20)
print(f"The type of {coordinates} is {type(coordinates)}.")  # Outputs: <class 'tuple'>

# 2. Using isinstance()
# The isinstance() function checks if an object is an instance of a specified class or type.

# Check if a variable is an integer
number = 42
print(f"{number} is an integer: {isinstance(number, int)}")  # Outputs: True

# Check if a variable is a string
text = "Hello"
print(f"'{text}' is a string: {isinstance(text, str)}")  # Outputs: True

# Check if a variable is a list
numbers_list = [1, 2, 3]
print(f"{numbers_list} is a list: {isinstance(numbers_list, list)}")  # Outputs: True

# Check if a variable is a tuple
coordinates = (10, 20)
print(f"{coordinates} is a tuple: {isinstance(coordinates, tuple)}")  # Outputs: True

# 3. Using id()
# The id() function returns a unique identifier for an object.
# This is useful for checking if two variables point to the same object in memory.

# Example with integers
a = 10
b = 10
print(f"The id of variable 'a' is {id(a)}.")  # Unique identifier of 'a'
print(f"The id of variable 'b' is {id(b)}.")  # Unique identifier of 'b'

# Example with lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"The id of list1 is {id(list1)}.")  # Unique identifier of 'list1'
print(f"The id of list2 is {id(list2)}.")  # Unique identifier of 'list2'

# Example of same object
list3 = list1
print(f"The id of list3 (which is the same as list1) is {id(list3)}.")  # Same id as list1

# Summary of Basic Data Handling Functions
# 1. type(): Identifies the type of an object (e.g., int, str, list).
# 2. isinstance(): Checks if an object is of a specified type or class.
# 3. id(): Provides a unique identifier for an object, useful for checking if two variables refer to the same object.

# Understanding these functions helps you to manage and debug your code by knowing the types of your data, validating data types, and checking object references.
