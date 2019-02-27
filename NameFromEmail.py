"""
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the
user name and company of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

john
google

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use \w to match letters.
"""

import re
abc = input('Enter email address: ')
# print(abc[0:abc.index('@', 0)])
# print(abc[abc.index('@', 0) + 1:abc.index('.', 0)])
pat1 = r'(\w+)@(\w+)\.(com)'
r1 = re.match(pat1, abc)
print(r1.group(1))
print(r1.group(2))
