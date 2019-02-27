"""
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
"""


class String:
    def __init__(self):
        self.string = ''

    def getstring(self, string):
        self.string = string

    def printstring(self):
        return self.string.upper()


if __name__ == '__main__':
    my_string = input("Please enter a string: ")
    s1 = String()
    s1.getstring(my_string)
    print(s1.printstring())
