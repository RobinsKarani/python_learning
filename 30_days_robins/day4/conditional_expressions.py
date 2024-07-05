a = 5
b = 10
c = 15

# Using nested ternary operators
result = "a is largest" if a > b and a > c else "b is largest" if b > c else "c is largest"

print(result)
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(f"Score: {score}, Grade: {grade}")
