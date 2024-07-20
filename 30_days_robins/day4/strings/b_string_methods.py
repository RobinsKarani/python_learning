# STRING METHODS

# 1. len()
# Returns the length of the string.
print(len("Python"))  # Output: 6
word2 = "Python"
print(len(word2))  # Output: 6

# 2 .lower() and .upper()
# Convert a string to lowercase or uppercase.
word = "Python"
print(word.lower())  # Output: python
print(word.upper())  # Output: PYTHON

# 3. count()
# Returns the number of characters in the string
word = "Python"
print(word.count())  # Output: 6

# 4. find()
# Returns the index of the character
word = "Python"
print(word.find('o'))  # Output: 4

# 5 .strip()
# Removes any leading and trailing whitespace.

text = "  Hello  "
print(text.strip())  # Output: Hello

# 6 .replace()
# Replace a substring with another substring.
# syntax string.replace(old_value, new_value, count)
# Parameter	Description
# old value	Required. The string to search for
# new value	Required. The string to replace the old value with
# count	Optional. A number specifying how many occurrences of the old value you want to replace.
# Default is all occurrences
text = "Hello, world!"
print(text.replace("world", "Python"))

# 7. split()
txt = "welcome to the jungle"
x = txt.split()  # output ['welcome', 'to', 'the', 'jungle']
print(x)

# 9.  .join()
# Joins elements of a list into a single string.
words = ["Hello", "world"]
joined_string = " ".join(words)
print(joined_string)  # Output: Hello world

