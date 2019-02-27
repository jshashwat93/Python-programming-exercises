"""
Question:
Define a class named American and its subclass NewYorker.

Hints:

Use class Subclass(ParentClass) to define a subclass.
"""


class American:
    @staticmethod
    def print_nationality():
        print('America')


class NewYorker(American):
    pass


a1 = American()
n1 = NewYorker()
a1.print_nationality()
American.print_nationality()
n1.print_nationality()
