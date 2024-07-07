# main.py
import mymodule

print(mymodule.greet("Alice"))  # Prints: Hello, Alice!
print(mymodule.add(3, 5))       # Prints: 8
# main.py
from mymodule import greet, add

print(greet("Alice"))  # Prints: Hello, Alice!
print(add(3, 5))       # Prints: 8

'''4. Aliasing
You can give a module or function a different name when you import it.
This is useful for shortening long module names or avoiding name conflicts.
'''
import mymodule as mm

print(mm.greet("Alice"))  # Prints: Hello, Alice!
print(mm.add(3, 5))       # Prints: 8