# mymodule.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b
# main.py
import mymodule

print(mymodule.greet("Alice"))  # Prints: Hello, Alice!
print(mymodule.add(3, 5))       # Prints: 8
