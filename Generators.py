"""
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
"""


def div_by_7(my_list):
    for j in my_list:
        if j % 7 == 0:
            yield j


if __name__ == '__main__':
    x = int(input("Enter a number: "))
    my_nums = div_by_7(range(1, x))
    for i in my_nums:
        print(i)
