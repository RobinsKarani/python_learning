operator = input("Enter an operator (+ - * /): ")
try:
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))

    if operator == "+":
        result = num1 + num2
        print(round(result, 3))
    elif operator == "-":
        result = num1 - num2
        print(round(result, 3))
    elif operator == "*":
        result = num1 * num2
        print(round(result, 3))
    elif operator == "/":
        if num2 == 0:
            print("Error! You can't divide a number by zero.")
        else:
            result = num1 / num2
            print(round(result, 3))
    else:
        print(f"{operator} is not a valid operator.")
except ValueError:
    print("Error, you've entered an invalid number.")
