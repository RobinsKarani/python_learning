# What is a String?
# A string is a sequence of characters enclosed in quotes.
# You can use single ('), double ("), triple single ('''),
# or triple double quotes (""") to define a string.

# examples
single_quote_string = 'Hello'
double_quote_string = "Hello"
triple_single_quote_string = '''Hello'''
triple_double_quote_string = """Hello"""

# Basic Operations
# 1.Concatenation
# You can concatenate (combine) strings using the + operator.
greeting = "Hello, " + "world!"
print(greeting)  # Output: Hello, world!

# 2.Repetition
# Use the * operator to repeat a string
repeat = "Ha" * 3
print(repeat)  # Output: HaHaHa
# you've just multiplied it by three.Strings ain't used in mathematical operations though

# 3.Indexing
# Access individual characters using indices (starting at 0)
word = "Python"
print(word[0])  # Output: P
print(word[-1])  # Output: n (negative index starts from the end)

# 4. Slicing
# Extract a substring using slicing.
word = "Python"
print(word[1:4])  # Output: yth (from index 1 to 3)
print(word[:2])  # Output: Py (from start to index 1)
print(word[4:])  # Output: on (from index 4 to the end)
print(word[:])  # Output: Python (whole string)

