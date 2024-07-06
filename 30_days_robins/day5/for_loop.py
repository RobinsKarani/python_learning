'''For Loop
A for keyword is used to make a for loop, similar with other programming languages,
but with some syntax differences. Loop is used for iterating over a sequence
(that is either a list, a tuple, a dictionary, a set, or a string).'''

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

    language = 'Python'
    for letter in language:
        print(letter)
        # string
    for i in range(len(language)):
        print(language[i])
        # tuples
        numbers = (0, 1, 2, 3, 4, 5)
        for number in numbers:
            print(number)

            #dictionary
            person = {
                'first_name': 'Asabeneh',
                'last_name': 'Yetayeh',
                'age': 250,
                'country': 'Finland',
                'is_marred': True,
                'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
                'address': {
                    'street': 'Space street',
                    'zipcode': '02210'
                }
            }
            for key in person:
                print(key)

            for key, value in person.items():
                print(key, value)  # this way we get both keys and values printed out
 # ** add loops in set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)