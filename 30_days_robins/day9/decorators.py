'''def my_decorator(func):  # func is the original function (say_hello)
    def wrapper():  # This is the new function that adds extra features
        print("Something before the function runs.")
        func()  # Call the original function (say_hello)
        print("Something after the function runs.")
    return wrapper  # Return the new function with the extra features
@my_decorator
def say_hello():
    print("Hello!")
'''


# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()
