"""
Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.
"""


def solve(num_heads, num_legs):
    for chickens in range(num_heads+1):
        rabbits = num_heads - chickens
        if 2 * chickens + 4 * rabbits == num_legs:
            return chickens, rabbits
    return 'No Solution'


heads = 35
legs = 94
solutions = solve(heads, legs)
print(solutions)
