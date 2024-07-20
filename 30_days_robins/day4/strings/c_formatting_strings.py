# method 1
# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The format() method returns the formatted string.
txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))
name = "Thiaine Robins"
txt2 = "my name is {name}"
print(txt2.format(name=name))

# f-Strings (Python 3.6+)
# Use f before the string and curly braces {} to insert variables.
name = "Nkirote"
print(f"My sister's {name}!")  # Output: My sister's Nkirote!

# Percent Formatting
# Use % operator for old-style formatting.
name = "Python"
print("Hello, %s!" % name)  # Output: Hello, Python!
# %s: String
# %d: Integer
# %f: Floating-point number
# %x: Hexadecimal integer

# General Syntax
# formatted_string = "format_string" % value

# Multiple Placeholders
name = "Robins"
age = 18
print("Hello, %s You are %d years old." % (name, age))

pi = 3.14159
print("Pi is approximately %f." % pi)  # Output: Pi is approximately 3.141590.
print("Pi is approximately %.2f." % pi)  # Output: Pi is approximately 3.14.

age = 25
print("I am %d years old." % age)  # Output: I am 25 years old.


