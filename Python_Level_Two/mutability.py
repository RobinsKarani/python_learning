#   decorator that accepts aergument

from functools import wraps

def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print("hello")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(5)
def my_function():
    """This is my function."""
    print("Function executed")

# Example usage
my_function()
