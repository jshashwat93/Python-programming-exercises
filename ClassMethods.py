"""
Question:
Define a class named American which has a static method called printNationality.

Hints:

Use @staticmethod decorator to define class static method.
"""


class American:
    @staticmethod
    def print_nationality():
        print('America')


a1 = American()
a1.print_nationality()
American.print_nationality()
