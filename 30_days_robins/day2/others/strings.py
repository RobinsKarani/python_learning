# Accessing Characters in Strings by Index
# In programming counting starts from zero.
# Therefore, the first letter of a string is at zero index and the last letter
# of a string is the length of a string minus one.
#
# String index

language = 'Python'
first_letter = language[0]
print(first_letter)  # P
second_letter = language[1]
print(second_letter)  # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)  # n

# If we want to start from right end we can use negative indexing. -1 is the last index.

language = 'Python'
last_letter = language[-1]
print(last_letter)  # n
second_last = language[-2]
print(second_last)  # o
