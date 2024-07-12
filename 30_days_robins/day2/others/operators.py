# Introduction
# Day 1 - 30DaysOfPython Challenge

print(2 + 3)   # addition(+)
print(3 - 1)   # subtraction(-)
print(2 * 3)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

# variables

x = 10
y = 5
print(x + y)  # variable addition

x = "Hello"

print(x + " World")  # variable concatenation

# data types

x = 10
y = 3.14
z = 1 + 3j

print(type(x))  # int

print(type(y))  # float

print(type(z))  # complex

# converting data types

x = 10
y = str(x)
print(y)  # converting int to string

x = 3.14

y = int(x)

print(y)  # converting float to int

x = 1 + 3j

y = float(x)

print(y)  # converting complex to float
