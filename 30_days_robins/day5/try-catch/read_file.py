
def read_file(file_path):

    try:
        # Attempt to open and read the file
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print("Error: The file was not found.")
    except IOError:
        # Handle other I/O related errors (e.g., permission denied)
        print("Error: An I/O error occurred.")
    except NameError:
        print('name not defined ')
    else:
        # If no exceptions were raised, this block will execute
        print("File read successfully!")
        print("File content:")
        print(content)
    finally:
        # This block will always execute
        print("Execution of file reading process is complete.")

# Example usage
file_path = 'example.txt'  # Replace with the path to your file
read_file(file_path)

