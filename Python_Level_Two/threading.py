# class CustomError(Exception):
#     pass
# try
#     pass
# except CustomError

class AgeError(Exception):
    "Raised when person age is less than 18"
    pass

try:
    age = float(input("Enter age: "))
    if(age < 18):
        raise AgeError
except AgeError:
    print("Person is not eligble to vote")
else:
    print("The pesron is elogble to vote")        
        
        