
name = "Alice"
age = 30
message = "%s is %d years old." % (name, age)
print(message)


'''Example 2: Using str.format()
Using the str.format() method is more powerful and flexible:'''

name = "Bob"
height = 1.75
message = "{} is {:.2f} meters tall.".format(name, height)
print(message)


'''Example 3: Using f-strings
f-strings are a new feature in Python 3.6 and
 are a great way to format strings in a more readable and concise way:'''


'''F-strings are the most modern and concise way to format strings:'''

name = "Charlie"
temperature = 23.456
message = f"{name}'s room temperature is {temperature:.1f}°C."
print(message)
{temperature:.1} # means "format the variable temperature as a floating-point number with 1 decimal place."
'''Output:
Charlie's room temperature is 23.5°C.'''

'''Common Format Specifiers
%s: String
%d: Decimal integer
%f: Floating-point number
%x: Hexadecimal integer
%o: Octal integer'''


'''Advanced Format Specifiers
%.<number>f: Floating-point number with <number> decimal places
%+d: Always include a sign (+ or -) for positive or negative numbers
%0<width>d: Pad the number with zeros to the specified width
%<width>.<precision>f: Pad the number with zeros to the specified width and <precision> decimal places
%<width>s: Pad the string with spaces to the specified width'''
product = "Milk"
price = 2.5
message = f"The price of {product} is ${price:6.2f}."
print(message)
'''6.2f means ("format as a floating-point number,"
 " with at least 6 characters wide, including 2 decimal places.")'''


''' Formatting Date and Time
Formatting date and time using datetime module:'''



from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"The current date and time is: {formatted_date}")
# %Y: Year with century
# %m: Month as a zero-padded decimal number
# %d: Day of the month as a zero-padded decimal number
# %H: Hour (24-hour clock) as a zero-padded decimal number
# %M: Minute as a zero-padded decimal number
# %S: Second as a zero-padded decimal number