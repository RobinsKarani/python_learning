# Write a Python program to create a class that represents a shape.
# Include methods to calculate its area and perimeter. 
# Implement subclasses for different shapes like circle, triangle, and square.
import math

class Shape:
    
    def area():
        pass
    def perimeter():
        pass

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
            
class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def area(self):
        s = (self.a + self.b +self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    

triangle1 = Triangle(3,4,5)
print(f"The area of the triangle is {triangle1.area():.2f} cm^2")