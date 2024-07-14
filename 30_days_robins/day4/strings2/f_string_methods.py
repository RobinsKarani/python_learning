# endswith(suffix)
# What it does: Checks if the string ends with a specified suffix.
#
# Use case: To verify if a filename ends with a certain extension, like .txt or .jpg.

filename = 'document.pdf'
print(filename.endswith('.pdf'))  # Output: True

#  find(substring)
# What it does: Finds the index of the first occurrence of a substring.
# Returns -1 if the substring is not found.
# Use case: When you need to locate where a specific word or character starts in a text.

text = 'hello world'
print(text.find('world'))  # Output: 6
