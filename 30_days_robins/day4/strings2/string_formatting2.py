# Old Style String Formatting (% Operator)
# In Python there are many ways of formatting strings.
# In this section, we will cover some of them.
# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list),
# together with a format string, which contains normal text together with "argument specifiers",
# special symbols like "%s", "%d", "%f", "%.number of digits".
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# "%.number of digitsf" - Floating point numbers with fixed precision
a = 4
b = 10

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))  # limits it to two decimal places
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# using f-string
print(f'{a},{b},{a-b}')
