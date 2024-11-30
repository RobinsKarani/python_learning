
def my_map(func,arguments_list):
    result = []
    for every_element in arguments_list:
        result.append(func(every_element))
    return result

def square(x):
    return x*x
2
def cube(x):
    return x*x*x


squares = my_map(square,[1,2,3,4,5])
cubes = my_map(cube,[1,2,3,4,5])    

print(squares)
print(cubes)