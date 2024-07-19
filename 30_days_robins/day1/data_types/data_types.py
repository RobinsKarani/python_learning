# Python Data Types Demonstration

# 1. Integers (int)
age = 25
negative_number = -10
print("Integers:")
print("Age:", age)
print("Negative number:", negative_number)
print("Type of age:", type(age))
print()

# 2. Floating-point numbers (float)
height = 1.75
pi = 3.14159
print("Floats:")
print("Height:", height)
print("Pi:", pi)
print("Type of height:", type(height))
print()

# 3. Strings (str)
name = "Alice"
greeting = 'Hello, World!'
print("Strings:")
print("Name:", name)
print("Greeting:", greeting)
print("Type of name:", type(name))
print()

# 4. Booleans (bool)
is_python_fun = True
is_coding_hard = False
print("Booleans:")
print("Is Python fun?", is_python_fun)
print("Is coding hard?", is_coding_hard)
print("Type of is_python_fun:", type(is_python_fun))
print()

# 5. Lists
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "two", 3.0, True]
print("Lists:")
print("Fruits:", fruits)
print("Mixed list:", mixed_list)
print("Type of fruits:", type(fruits))
print()

# 6. Tuples
coordinates = (10, 20)
rgb_color = (255, 0, 128)
print("Tuples:")
print("Coordinates:", coordinates)
print("RGB Color:", rgb_color)
print("Type of coordinates:", type(coordinates))
print()

# 7. Dictionaries
person = {
    "name": "Bob",
    "age": 30,
    "city": "New York"
}
print("Dictionary:")
print("Person:", person)
print("Person's name:", person["name"])
print("Type of person:", type(person))
print()

# Demonstrating type conversion
string_number = "42"
converted_number = int(string_number)
print("Type Conversion:")
print("String '42':", string_number, "- Type:", type(string_number))
print("Converted to integer:", converted_number, "- Type:", type(converted_number))

