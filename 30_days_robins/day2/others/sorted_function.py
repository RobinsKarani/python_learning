# sorted() function basics
# sorted(iterable, key=None, reverse=False)

# Basic usage
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
sorted_numbers = sorted(numbers)
print("Original list:", numbers)
print("Sorted list:", sorted_numbers)

# The original list remains unchanged
print("Original list after sorting:", numbers)

# Sorting in descending order
desc_sorted = sorted(numbers, reverse=True)
print("Sorted in descending order:", desc_sorted)

# Sorting strings
fruits = ['banana', 'apple', 'cherry', 'date']
sorted_fruits = sorted(fruits)
print("\nSorted fruits:", sorted_fruits)

# Sorting by length of strings using a key function
sorted_by_length = sorted(fruits, key=len)
print("Sorted by length:", sorted_by_length)


# Custom sorting with a key function
def last_letter(s):
    return s[-1]


sorted_by_last_letter = sorted(fruits, key=last_letter)
print("Sorted by last letter:", sorted_by_last_letter)

# Sorting dictionaries
scores = {'Alice': 88, 'Bob': 72, 'Charlie': 95, 'David': 80}
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print("\nSorted scores:", sorted_scores)


# Sorting objects
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"Student(name='{self.name}', grade={self.grade})"


students = [
    Student('Alice', 88),
    Student('Bob', 72),
    Student('Charlie', 95),
    Student('David', 80)
]

sorted_students = sorted(students, key=lambda student: student.grade, reverse=True)
print("\nSorted students:", sorted_students)

# Using operator.itemgetter and operator.attrgetter for more efficient key functions
from operator import itemgetter, attrgetter

# Sorting list of tuples
data = [('Alice', 88), ('Bob', 72), ('Charlie', 95), ('David', 80)]
sorted_data = sorted(data, key=itemgetter(1), reverse=True)
print("\nSorted data using itemgetter:", sorted_data)

# Sorting list of objects more efficiently
sorted_students_efficient = sorted(students, key=attrgetter('grade'), reverse=True)
print("Sorted students using attrgetter:", sorted_students_efficient)