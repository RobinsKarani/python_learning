# 2. Write a Python program to create a person class.
#  Include attributes like name, country and date of birth.
#  Implement a method to determine the person's age.

# importing datetime module for now()
import datetime

class Person:

    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = dob

    def age(self):
        today = datetime.date.today()
        age = today.year - self.dob.year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        
        return age

name = input("Enter your name: ")
country = input("Enter the name of your country: ")
year = int(input("Enter the yr of birth(YY): "))
month = int(input("Enter the month of birth(MM): "))
day = int(input("Enter the day of birth(DD): "))

dob = datetime.date(year,month,day)
        
person1 = Person(name,country,dob)

print(f"\nName: {person1.name}")
print(f"Country: {person1.country}")
print(f"Date of Birth: {person1.dob}")
print(f"Age: {person1.age()} years")