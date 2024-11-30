def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

# Create a multiplier function that multiplies by 2
multiply_by_2 = create_multiplier(2)

# Use it
print(multiply_by_2(5))  # Output: 10
