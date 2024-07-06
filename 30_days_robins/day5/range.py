'''1. range(stop)
This generates numbers from 0 to stop - 1.

Real-life Example:
Imagine you are a coach, and you want to count the number of laps your team runs from
0 to 9.'''

for lap in range(10):
    print("Lap:", lap)


'''range(start, stop)
This generates numbers from start to stop - 1.

Real-life Example:
Imagine you are a teacher, and you want to assign student IDs starting from 5 up to 9.'''

for student_id in range(5, 10):
    print("Student ID:", student_id)



'''3. range(start, stop, step)
This generates numbers from start to stop - 1, incrementing by step.
If step is negative, it decrements.

Real-life Example:
Imagine you are counting down to a rocket launch from 10 to 1.'''

for countdown in range(10, 0, -1):
    print("Countdown:", countdown)
'''Visual Example
Imagine a staircase:

range(5) would be like counting the steps from the ground (0) to the 4th step.
range(2, 6) would be like starting at the 2nd step and counting up to the 5th step.
range(10, 1, -2) would be like starting at the 10th step and
 counting down every 2 steps until you reachthe 2nd step.
By using the range function, you can control how you count through iterations,
 just like counting steps on a staircase,
 making it very useful in loops for repeating actions a specific number of times.'''