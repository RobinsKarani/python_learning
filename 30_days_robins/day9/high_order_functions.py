
# using function as a parameter
def sum_numbers(nums):  # normal function
    return sum(nums)  # a sad function abusing the built-in sum function :<

def higher_order_function(random_function, list_of_numbers):  # function as a parameter
    summation = random_function(list_of_numbers)
    return summation


result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)  # 15

# Function as a Return Value

