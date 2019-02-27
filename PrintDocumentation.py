"""
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some
books. But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function

Hints:
    The built-in document method is __doc__
"""

print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)


def square(num):
    """Return the square value of the input number.

    The input number must be integer.
    """
    return num ** 2


print(square(2))
print(square.__doc__)

"""
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even,
otherwise print "It is an odd number".
"""