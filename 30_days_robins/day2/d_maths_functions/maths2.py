import math
import random
import statistics

# Random number generation
random_int = random.randint(1, 10)  # Random integer between 1 and 10 (inclusive)
random_float = random.random()  # Random float between 0 and 1
random_range = random.uniform(1, 10)  # Random float between 1 and 10

# List of numbers for statistical operations
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Basic statistics
mean_value = statistics.mean(numbers)  # Average of the numbers
median_value = statistics.median(numbers)  # Middle value of the sorted numbers
mode_value = statistics.mode(numbers)  # Most common value in the list
stdev_value = statistics.stdev(numbers)  # Standard deviation of the numbers

# More advanced math functions
factorial_value = math.factorial(5)  # 5! = 5 * 4 * 3 * 2 * 1 = 120
gcd_value = math.gcd(48, 18)  # Greatest Common Divisor of 48 and 18

# Degree-radian conversion
degrees = 45
radians = math.radians(degrees)  # Convert degrees to radians
degrees_again = math.degrees(radians)  # Convert radians back to degrees

# Complex numbers(not necessary, but you can research more on them)
complex_num = complex(3, 4)  # Create a complex number: 3 + 4i
real_part = complex_num.real  # Get the real part (3)
imag_part = complex_num.imag  # Get the imaginary part (4)
# ignore this.magnitude = abs(complex_num)  # Get the magnitude (5)

