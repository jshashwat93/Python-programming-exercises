"""
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


import math


pos = [0, 0]
while True:
    move = input("Enter move: ")
    if not move:
        break
    move = move.split()
    direction = move[0]
    distance = int(move[1])
    if direction == 'UP':
        pos[0] = pos[0] + distance
    elif direction == 'DOWN':
        pos[0] = pos[0] - distance
    elif direction == 'RIGHT':
        pos[1] = pos[1] + distance
    elif direction == 'LEFT':
        pos[1] = pos[1] - distance
print(round((math.sqrt((pos[0] ** 2) + (pos[1] ** 2)))))

