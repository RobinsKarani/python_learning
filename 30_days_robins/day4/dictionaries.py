'''Dictionaries
A dictionary is a collection of unordered,
modifiable(mutable) paired (key: value) data type.
Creating a Dictionary
To create a dictionary we use curly brackets, {} or the dict() built-in function.
'''
# Dictionary
person = dict(first_name='Robinson',
              last_name='`Thiaine',
              age=18, country='Kenya',
              occupation='Engineer',
              techStack=['Python', 'Flutter', 'gRPC', 'FastAPI'],
              interests=['Systems Engineering',
                         'Backend Development',
                         'Startups',
                         'AR & AI'
                         ],
              address={
                  'street': '',
                  'zipcode': ''
              })
print(person.get('first_name'))
print(person.get('country'))
print(person.get('skills'))
print(person.get('city'))

'''Changing Dictionary to a List of Items
The items() method changes dictionary to a list of tuples.'''

# syntax
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct.items())
