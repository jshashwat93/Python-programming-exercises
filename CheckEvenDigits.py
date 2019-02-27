"""
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the
number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


my_list = []
for n in range(1000,3001):
    n = str(n)
    odd = False
    for x in n:
        if int(x) % 2 != 0:
            odd = True
    if odd is False:
        my_list.append(n)
print(','.join(my_list))
