# Task: Create a Simple Calculator with a Menu
# Build a program that acts as a simple calculator. The program should:

# Allow the user to select an operation from a menu 
# (e.g., addition, subtraction, multiplication, or division).
# Ask the user to input two numbers.
# Perform the operation and display the result.
# Allow the user to perform multiple calculations in a loop until they decide to quit.
# Handle errors, such as invalid input or division by zero.

val1 = float(input("Enter value1: "))
val2 = float(input("Enter value2: "))
operator = input("Enter the operator: ")
class Calculator:
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2
        
        
    def add(self):
        return self.value1 + self.value2
    def subtract(self):
        return self.value1 - self.value2
    def divide(self):
        if self.value2 == 0:
            raise ZeroDivisionError("Cannot divide by 0")
        return self.value1/self.value2
    def multiply(self):
        return self.value1 * self.value2
    


calculate = Calculator(val1,val2)
if operator == "+":
    print(calculate.add())   
elif operator == "-":
    print(calculate.subtract()) 
elif operator == "*":
    print(calculate.multiply())
elif operator == "/":
    print(calculate.divide())
else:
    print("Invalid operator")
    

    
    
        
        
    

    
