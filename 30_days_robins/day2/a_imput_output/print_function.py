# You can create a separate file for running small blocks of code to test their output

# 1. print()
"""The print() function is used to display information to the console.
It's commonly used for debugging, showing results, or providing information to the user."""
# Basic Usage
# The print() function is used to output text or other data to the console.
print("Hello, world!")  # Outputs: Hello, world!

# Printing Multiple Items
'''You can print multiple items by separating them with commas.
 The print() function adds a space between each item by default.'''

name = "Alice"
age = 30
print("Name:", name, "Age:", age)  # Outputs: Name: Alice Age: 30

# Using the sep Parameter
# The sep parameter allows you to change the separator between multiple items.
print("apple", "banana", "cherry", sep=", ")  # Outputs: apple, banana, cherry

# Using the end Parameter
""" The end parameter specifies what to print at the end of the output.
 By default, it’s a newline character (\n), but you can change it to any string."""
print("Hello", end=" ")
print("world!")  # Outputs: Hello world!

# Printing Variables and Expressions
# You can print variables and the results of expressions.
x = 5
y = 10
print("The sum of", x, "and", y, "is", x + y)  # Outputs: The sum of 5 and 10 is 15
# x+y is the expression, x and y are variables

# String Formatting
# Using the format() Method
# The format() method allows you to insert variables into strings.
name = "RobinsKarani"
age = 18
print("Name: {}, Age: {}".format(name, age))  # Outputs: Name: RobinsKarani, Age: 18

# Using f-Strings (Formatted String )
# f-Strings (available in Python 3.6+) provide a more readable way to format strings.
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")  # Outputs: Name: Alice, Age: 30
# compare with old style i.e: print("Name: {}, Age: {}".format(name, age))

# Escaping Characters
# If you need to include special characters like quotes within a string, you can escape them using a backslash (\).
print("He said, \"Hello, world!\"")  # Outputs: He said, "Hello, world!"

# Printing with Newlines and Tabs
# You can include newline (\n) and tab (\t) characters in your strings.
print("Line 1\nLine 2")  # Outputs:
# Line 1
# Line 2

print("Column 1\tColumn 2")  # Outputs: Column 1    Column 2
# \t indicates tabSpace

# Printing Lists and Dictionaries
# You can print lists, dictionaries, and other data types directly.
my_list = [1, 2, 3]
my_dict = {"name": "Alice", "age": 30}
print(my_list)  # Outputs: [1, 2, 3]
print(my_dict)  # Outputs: {'name': 'Alice', 'age': 30}

# Redirecting Output to a File.'''You can skip this if you don gerrit''' ,
'''you may not understand this, but you can consult chatgpt or any other
 relevant source'''
# You can use the file parameter to redirect the output to a file.
with open("output.txt", "w") as file:
    print("Hello, file!", file=file)

# Common Pitfalls

# Forgetting Parentheses (Python 3.x)
# In Python 3, print is a function and requires parentheses.

# Incorrect (Python 2.x style):
# print "Hello, world!"

# Correct (Python 3.x style):
print("Hello, world!")

# Mixing Data Types
''' If you try to concatenate strings and numbers directly, you’ll get an error.
 Use commas or str() to convert numbers to strings.'''

# Incorrect:
# age = 30
# print("Age: " + age)  # TypeError: can only concatenate str (not "int") to str

# Correct:
age = 30
print("Age:", age)
# or
print("Age: " + str(age))

# str(age) means converting age to string

# Don't mind if you ain't getting anything ,you'll keep coming across that stuff till you'll understand
# feel free to reach out for any clarification.Otherwise,you can use chatGPT,claude or any other Chatbot
