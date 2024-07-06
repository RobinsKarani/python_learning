count = 1
while count < 11:
    print(count)
    count = count + 1
# prints from 1 to 10
count = 0 # 7
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# break
# we use break when we want to get out of the loop
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

 # Continue: With the continue statement we can skip the current iteration, and continue with the next:
  # syntax
'''while condition:
    code goes here
    if another_condition:
        continue'''
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
'''Explanation
The loop runs as long as i is less than 10.
Each iteration increments i by 1.
If i is an even number (i.e., i % 2 == 0),
the continue statement is executed, skipping the print(i) statement and starting the next iteration.
If i is an odd number, it gets printed.'''