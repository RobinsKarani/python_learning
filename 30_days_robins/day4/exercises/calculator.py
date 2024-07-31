firstnumber = float(input('enter the first number: \n'))
secondnumber = float(input('enter the second number: \n'))
operator = input('enter the operator(+,-,*,/)')

if operator == '+':
    result = firstnumber + secondnumber
    print(f'The sum of {firstnumber} and {secondnumber} is {result}')
elif operator == '-':
    result = firstnumber - secondnumber
    print(f'The difference of {firstnumber} and {secondnumber} is {result}')
elif operator == '*':
        result = firstnumber * secondnumber
        print(f'The product of {firstnumber} and {secondnumber} is {result}')
elif operator == '/':
    if secondnumber == 0:
        print('Error! Division by zero is not allowed.')
    else:
        result = firstnumber / secondnumber
        print(f'The quotient of {firstnumber} and {secondnumber} is {result}')


