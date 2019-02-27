"""
Write a program which can map() and filter() to make a list whose elements are square of even number in
[1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.
"""


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
anon = map(lambda a: a ** 2, filter(lambda a: a % 2 == 0, x))
for i in anon:
    print(i)
