"""
Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:

Use try/except to catch exceptions.
"""


try:
    print(5/0)
except ZeroDivisionError as e:
    print(e)


"""
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the
user name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

john

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use \w to match letters.
"""




