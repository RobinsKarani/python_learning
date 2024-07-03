
# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

# Updating a variable

first_name = 'John'
print('Updated first name:', first_name)

# Deleting a variable

del first_name
print('First name after deletion:', first_name)  # This will throw an error because the variable has been deleted


""" Dictionary (dict)
Definition: A dictionary is a collection of key-value pairs.
Syntax: {key1: value1, key2: value2}
Mutable: Yes, dictionaries are mutable, meaning you can change, add, or remove items.
Order: Since Python 3.7, dictionaries maintain the insertion order.
Access: Values are accessed using keys, e.g., dict[key].
Use Case: Useful for fast lookups, and associating keys with values.
Example """


my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict["name"])  # Output: Alice


# Accessing values using get() method

print(my_dict.get("name"))  # Output: Alice
print(my_dict.get("occupation", "Unknown"))  # Output: Unknown


# Updating a dictionary

my_dict["age"] = 31
print(my_dict)  # Output: {"name": "Alice", "age": 31, "city": "New York"}


# Adding a new key-value pair

my_dict["occupation"] = "Engineer"
print(my_dict)  # Output: {"name": "Alice", "age": 31, "city": "New York", "occupation": "Engineer"}


# Removing a key-value pair

del my_dict["city"]
print(my_dict)  # Output: {"name": "Alice", "age": 31, "occupation": "Engineer"}


# Checking if a key exists in a dictionary

print("name" in my_dict)  # Output: True
print("gender" in my_dict)  # Output: False


# Iterating over a dictionary

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")


# Converting a dictionary to a list of tuples

dict_list = list(my_dict.items())
print(dict_list)  # Output: [('name', 'Alice'), ('age', 31), ('occupation', 'Engineer')]


# Converting a list of tuples back to a dictionary

dict_from_list = dict(dict_list)
print(dict_from_list)  # Output: {'name': 'Alice', 'age': 31, 'occupation': 'Engineer'}


# Checking the length of a dictionary

print(len(my_dict))  # Output: 3


""" Tuples (tuple)
Definition0: A tuple is a collection of items separated by commas.
Definition1: A tuple is an ordered collection of items which can be of different types.
Syntax: (item1, item2, item3)
Immutable: Yes, tuples are immutable, meaning you cannot change, add, or remove items.
Order: Tuples maintain the order of elements.
Access: Elements are accessed using indexing, e.g., tuple[index].
Use Case: Useful for fixed collections of items, and as keys in dictionaries due to their immutability.

 """

my_tuple = ("Alice", 30, "New York")
print(my_tuple[0])  # Output: Alice


# Updating a tuple

my_tuple[1] = 31  # This will raise a TypeError

print(my_tuple)  # Output: ('Alice', 31, 'New York')



# Converting a tuple to a list

my_list = list(my_tuple)
print(my_list)  # Output: ['Alice', 31, 'New York']


# Converting a list back to a tuple

my_tuple_from_list = tuple(my_list)
print(my_tuple_from_list)  # Output: ('Alice', 31, 'New York')


# Checking the length of a tuple

print(len(my_tuple))  # Output: 3


# Using a tuple as a key in a dictionary

my_dict = {"Alice": 30, "Bob": 25, "Charlie": 35}
print(my_dict["Alice"])  # Output: 30


# Using a tuple as a key in a set

my_set = {"Alice", "Bob", "Charlie"}
print("Alice" in my_set)  # Output: True


# Converting a tuple to a set

my_set = set(my_tuple)
print(my_set)  # Output: {'Alice', 30, 'Charlie', 35, 'Bob'}


# Converting a set back to a tuple

my_tuple_from_set = tuple(my_set)
print(my_tuple_from_set)  # Output: ('Alice', 30, 'Charlie', 35, 'Bob')


# Checking the length of a set

print(len(my_set))  # Output: 5

#Lists

my_list = ["Alice", "Bob", "Charlie"]
print(my_list[0])  # Output: Alice


# Updating a list

my_list[1] = "Bobbie"
print(my_list)  # Output: ['Alice', 'Bobbie', 'Charlie']


# Adding an item to the end of a list

my_list.append("David")
print(my_list)  # Output: ['Alice', 'Bobbie', 'Charlie', 'David']


# Adding an item at a specific index

my_list.insert(1, "Billy")
print(my_list)  # Output: ['Alice', 'Billy', 'Bobbie', 'Charlie', 'David']


# Removing an item by value

my_list.remove("Bobbie")
print(my_list)  # Output: ['Alice', 'Billy', 'Charlie', 'David']


# Removing an item by index

my_list.pop(1)
print(my_list)  # Output: ['Alice', 'Charlie', 'David']


# Reversing a list

my_list.reverse()
print(my_list)  # Output: ['David', 'Charlie', 'Alice']


# Sorting a list

my_list.sort()
print(my_list)  # Output: ['Alice', 'Charlie', 'David']


# Checking if an item exists in a list

print("Alice" in my_list)  # Output: True


""" Set (set)
Definition: A set is an unordered collection of unique items.
Syntax: {item1, item2, item3} or set([item1, item2, item3])
Mutable: Yes, sets are mutable, but you can also create an immutable set using frozenset.
Order: Sets are unordered, so the order of elements is not preserved.
Access: Elements are accessed through iteration, not indexing.
Use Case: Useful for membership testing, eliminating duplicate entries, and mathematical operations like union, intersection.
Example:
 """

my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  # Output: True

#adding
my_set.add(6)

#whole set
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# removing item from a set
my_set.remove(3)

#whole set after removing

print(my_set)  # Output: {1, 2, 4, 5, 6}

#union

set1 = {1, 2, 3}
set2 = {2, 3, 4}

union_set = set1.union(set2)

print(union_set)  # Output: {1, 2, 3, 4}

#intersection

intersection_set = set1.intersection(set2)

print(intersection_set)  # Output: {2, 3}

#difference

difference_set = set1.difference(set2)

print(difference_set)  # Output: {1}

#symmetric difference

symmetric_difference_set = set1.symmetric_difference(set2)

print(symmetric_difference_set)  # Output: {1, 4}

#issubset





