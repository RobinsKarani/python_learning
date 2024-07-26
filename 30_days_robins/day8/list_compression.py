'''For instance if you want to change a string to a list of characters.
You can use a couple of methods. Let's see some of them:
'''
# One way
language = 'Python'
lst = list(language)  # changing the string to list
print(type(lst))  # list
print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst))  # list
print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']

# Number of rows in the triangle
n = 5

# List comprehension to generate the triangle
triangle = ['*' * (i + 1) for i in range(n)]

# Print each row of the triangle
for everyRow in triangle:
    print(everyRow)

    '''# Generating even numbers
    even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
    print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    # Generating odd numbers
    odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
    print(odd_numbers)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    # Filter numbers: let's filter out positive even numbers from the list below
    numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
    positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
    print(positive_even_numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    # Flattening a three dimensional array
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened_list = [number for row in list_of_lists for number in row]
    print(flattened_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
    # Flattening a three-dimensional array
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened_list = [i for i in list_of_lists]
    print(flattened_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Nested lists representing different sections of the store with products
    store_inventory = [
        ["Apples", "Bananas", "Oranges"],
        ["Milk", "Cheese", "Yogurt"],
        ["Bread", "Bagels", "Croissants"]
    ]

    # Flatten the nested lists into a single list of all products in the store
    all_products = [product for section in store_inventory for product in section]

    # Print the flattened list of products
    print("Store Inventory:")
    for index, product in enumerate(all_products, start=1):
        print(f"{index}. {product}")

    # Output:
    # Store Inventory:
    # 1. Apples
    # 2. Bananas
    # 3. Oranges
    # 4. Milk
    # 5. Cheese
    # 6. Yogurt
    # 7. Bread
    # 8. Bagels
    # 9. Croissants
# lambda function

