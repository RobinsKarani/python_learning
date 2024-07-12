# File Handling in Python

# 1. Using open()
# The open() function is used to open a file and returns a file object.
# It takes two main arguments:
# - file name: The name of the file you want to open.
# - mode: The mode in which you want to open the file. Common modes include:
#   - 'r' for reading (default mode)
#   - 'w' for writing (creates a new file or truncates the existing file)
#   - 'a' for appending (adds content to the end of the file)
#   - 'b' for binary mode
#   - 't' for text mode (default mode)

# Example: Opening a file in read mode
file = open('example.txt', 'r')  # Opens 'example.txt' for reading

# Perform some file operations (e.g., reading content)
content = file.read()  # Reads the entire content of the file
print(content)  # Prints the content of the file

# 2. Using close()
# The close() function is used to close an open file.
# It is important to close a file after you're done with it to free up system resources.

file.close()  # Closes the file

# Note: It's a good practice to use the 'with' statement to open files, which ensures proper closure of the file.
# The file is automatically closed when the block inside the 'with' statement is exited, even if an exception occurs.

# Example: Using 'with' statement to open and close a file automatically
with open('example.txt', 'r') as file:
    content = file.read()  # Reads the entire content of the file
    print(content)  # Prints the content of the file
# The file is automatically closed here

# 3. Writing to a file
# Example: Opening a file in write mode and writing content to it
with open('example_write.txt', 'w') as file:
    file.write("Hello, world!\n")  # Writes a line of text to the file
    file.write("This is a file handling example.\n")  # Writes another line of text to the file
# The file is automatically closed here

# 4. Appending to a file
# Example: Opening a file in append mode and adding content to it
with open('example_write.txt', 'a') as file:
    file.write("Adding a new line at the end.\n")  # Appends a line of text to the file
# The file is automatically closed here

# Summary of File Handling
# 1. open(): Opens a file and returns a file object. Modes include 'r', 'w', 'a', 'b', 't'.
# 2. close(): Closes an open file. It's important to close files to free up system resources.
# 3. Use 'with' statement: Ensures the file is properly closed after operations.

# These functions and practices are essential for working with files in Python,
# enabling you to read from and write to files safely and efficiently.
