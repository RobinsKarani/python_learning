"""Python Closures
Python allows a nested function to access the outer scope of the enclosing function.
This is known as a Closure. Let us have a look at how closures work in Python.
In Python, closure is created by nesting a function inside another encapsulating function
and then returning the inner function. See the example below.
"""


def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20