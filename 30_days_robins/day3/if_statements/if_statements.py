# age = 25
#
# if age >= 18 and age <= 65:
#     print("You are an adult.")
# else:
#     print("You are either a minor or a senior citizen.")
 # nested if
age = 25
if age >= 18:
     print("You are an adult.")
     if age <= 65:
         print("You are an adult within the age range.")
     else:
         print("You are a senior citizen.")