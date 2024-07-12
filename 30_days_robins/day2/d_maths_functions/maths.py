# https://docs.python.org/3/library/math.html
# Basic arithmetic operations
a = 10
b = 3

addition = a + b  # Addition: 10 + 3 = 13
subtraction = a - b  # Subtraction: 10 - 3 = 7
multiplication = a * b  # Multiplication: 10 * 3 = 30
division = a / b  # Division: 10 / 3 = 3.3333... (returns a float)
integer_division = a // b  # Integer division: 10 // 3 = 3 (rounds down)
modulus = a % b  # Modulus (remainder): 10 % 3 = 1
exponentiation = a ** b  # Exponentiation: 10 ** 3 = 1000

# Built-in math functions
import math

c = -4.7
d = 2.5

abs_value = abs(c)  # Absolute value: |-4.7| = 4.7
rounded = round(d)  # Round to nearest integer: 2.1 rounds to 2
ceiling = math.ceil(d)  # Ceiling (round up): ceil(2.1) = 3
floor = math.floor(d)  # Floor (round down): floor(2.1) = 2

# Trigonometric functions (input in radians)
angle = math.pi / 4  # 45 degrees in radians

sin_value = math.sin(angle)  # Sine of 45 degrees
cos_value = math.cos(angle)  # Cosine of 45 degrees
tan_value = math.tan(angle)  # Tangent of 45 degrees

# Logarithmic and exponential functions(not so necessary)
e = math.e  # Euler's number (approximately 2.71828)
natural_log = math.log(e)  # Natural logarithm of e (equals 1)
log_10 = math.log10(100)  # Base-10 logarithm of 100 (equals 2)
exp_value = math.exp(2)  # e raised to the power of 2

# Square root and power~necessary
sqrt_value = math.sqrt(16)  # Square root of 16 (equals 4)
power_value = pow(2, 3)  # 2 raised to the power of 3 (equals 8)

# Constants
pi = math.pi  # Pi (approximately 3.14159)
