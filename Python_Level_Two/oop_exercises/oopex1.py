# Write a Python program to create a class representing a Circle.
# Include methods to calculate its area and perimeter.
import math

# Get radius input from the user
the_radius = float(input("Enter the radius of the Circle: "))

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def circumference(self):
        """Calculate the circumference of the circle."""
        return 2 * math.pi * self.radius 

# Create a Circle instance and display results
circle1 = Circle(the_radius)
print(f"Area: {circle1.area():.2f}")    
print(f"Circumference: {circle1.circumference():.2f}")
