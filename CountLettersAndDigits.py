"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

x = input("Enter a sentence: ")
x = x.replace(" ", "")
letters = 0
digits = 0
for n in x:
    if n.isalpha():
        letters += 1
    elif n.isnumeric():
        digits += 1
print('LETTERS {}\nDIGITS {}'.format(letters, digits))