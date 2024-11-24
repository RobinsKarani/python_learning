# Write a Python program to create a calculator class.
#  Include methods for basic arithmetic operations.

class Calculator:
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2
        
    def add(self):
        return self.value1 + self.value2
    def sutract(self):
        return self.value1 - self.value2
    def multiply(self):    
        return self.value1 * self.value2
    def divide(self):
        if self.value2 != 0:
            return self.value1/self.value2
        else:
            return "***Cannot divide by Zero!!***"
            
        
value1 = float(input("Enter value 1: "))
value2 = float(input("Ebter value 2: "))       

calculation1 = Calculator(value1,value2)    

print(calculation1.divide())    
                 


        