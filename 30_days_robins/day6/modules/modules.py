'''
 A Module is a file containing a set of codes or a set of functions which can be included to an application. A module could be a file containing a single variable, a function or a big code base.

Creating a Module
To create a module we write our codes in a python script and we save it as a .py file. Create a file named mymodule.py inside your project folder. Let us write some code in this file.

# mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
Create main.py file in your project directory and import the mymodule.py file.

Importing a Module
To import the file we use the import keyword and the name of the file only.

# main.py file
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh'''