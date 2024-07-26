import builtins

# Get all built-in function names
builtin_functions = [name for name in dir(builtins) if callable(getattr(builtins, name))]

# Print the list of built-in function names
print("List of all built-in functions:")
for func in builtin_functions:
    print(func)

# Print the total count
print(f"\nTotal number of built-in functions: {len(builtin_functions)}")