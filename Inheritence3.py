"""
Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print
"Male" for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.
"""


class Person:
    def __init__(self):
        self.gender = 'None'

    def get_gender(self):
        return self.gender


class Male(Person):
    def __init__(self):
        super().__init__()
        self.gender = 'Male'


class Female(Person):
    def __init__(self):
        super().__init__()
        self.gender = 'Female'


if __name__ == '__main__':
    p1 = Person()
    m1 = Male()
    f1 = Female()
    print(p1.get_gender())
    print(m1.get_gender())
    print(f1.get_gender())
