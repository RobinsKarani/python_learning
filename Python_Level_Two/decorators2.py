age = 41  # Change this value to test

def ensure_positive(func):
    def ispositive(*args, **kwargs):
        if args[0] > 0:
            return func(*args, **kwargs)
        return "The number must be positive"
    return ispositive

@ensure_positive
def his_age(age):
    print(f"The age is: {age}")
    return "end"

# Call the function with age
print(his_age(age))  # Test with the current value of `age`
