# Sequence Operations in Python

# 1. Using len()
# The len() function returns the length of a sequence (like a string, list, or tuple).

# Example with a string
text = "Hello, world!"
text_length = len(text)  # Returns the number of characters in the string
print(f"The length of the string '{text}' is {text_length}.")

# Example with a list
numbers = [1, 2, 3, 4, 5]
list_length = len(numbers)  # Returns the number of elements in the list
print(f"The length of the list {numbers} is {list_length}.")

# Example with a tuple
coordinates = (10, 20, 30)
tuple_length = len(coordinates)  # Returns the number of elements in the tuple
print(f"The length of the tuple {coordinates} is {tuple_length}.")

# 2. Using range()
# The range() function generates a sequence of numbers. It's often used in loops.

# Example of range with one argument (generates numbers from 0 up to, but not including, 5)
for i in range(5):
    print(i, end=" ")  # Outputs: 0 1 2 3 4
print()  # Newline for clean output

# Example of range with two arguments (generates numbers from 2 up to, but not including, 5)
for i in range(2, 5):
    print(i, end=" ")  # Outputs: 2 3 4
print()

# Example of range with three arguments (generates numbers from 0 up to, but not including, 10, with a step of 2)
for i in range(0, 10, 2):
    print(i, end=" ")  # Outputs: 0 2 4 6 8
print()

# 3. Using list()
# The list() function converts a value to a list.

# Converting a string to a list (each character becomes an element of the list)
char_list = list("Python")
print(f"The string 'Python' as a list is {char_list}.")

# Converting a tuple to a list
numbers_tuple = (1, 2, 3, 4, 5)
numbers_list = list(numbers_tuple)  # Converts the tuple to a list
print(f"The tuple {numbers_tuple} as a list is {numbers_list}.")

# 4. Using tuple()
# The tuple() function converts a value to a tuple.

# Converting a list to a tuple
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)  # Converts the list to a tuple
print(f"The list {fruits_list} as a tuple is {fruits_tuple}.")

# Converting a string to a tuple (each character becomes an element of the tuple)
char_tuple = tuple("Python")
print(f"The string 'Python' as a tuple is {char_tuple}.")

# 5. Using set()
# The set() function converts a value to a set.
# Sets are collections of unique elements and automatically remove duplicates.

# Converting a list to a set (removes duplicate elements)
numbers_list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
numbers_set = set(numbers_list_with_duplicates)  # Converts the list to a set, removing duplicates
print(f"The list {numbers_list_with_duplicates} as a set is {numbers_set}.")

# Converting a string to a set (removes duplicate characters)
char_set = set("hello")
print(f"The string 'hello' as a set is {char_set}.")  # Output may vary in order, e.g., {'h', 'e', 'l', 'o'}

# Summary of Sequence Operations
# 1. len(): Measures the length of sequences like strings, lists, and tuples.
# 2. range(): Generates sequences of numbers, useful for looping.
# 3. list(): Converts strings, tuples, or other iterables into lists.
# 4. tuple(): Converts lists, strings, or other iterables into tuples.
# 5. set(): Converts iterables into sets, automatically removing duplicates.

# These operations help manipulate and manage sequences in Python,
# making it easier to work with collections of data.
