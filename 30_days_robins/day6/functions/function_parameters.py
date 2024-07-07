def greet(name):
    return f"Hello, {name}!"

def call_function(func, argument):
    return func(argument)

print(call_function(greet, "Alice"))  # Prints: Hello, Alice!

'''3. Arbitrary Arguments (Args and Kwargs)
Positional Arguments (*args)
You can use *args to accept an arbitrary number of positional arguments.
This is useful when you don't know in advance how many arguments will be passed to the function.'''

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))         # Prints: 6
print(sum_all(5, 10, 15, 20))   # Prints: 50