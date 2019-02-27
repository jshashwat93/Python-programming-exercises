"""
A website requires the users to input username and password to register. Write a program to check the validity of
password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


import re
x = input("Enter CSV passwords: ")
x = x.split(',')
legal_password = []
for n in x:
    rule = True
    if not re.search("[a-z]", n):
        rule = False
    if not re.search("[0-9]", n):
        rule = False
    if not re.search("[A-Z]", n):
        rule = False
    if not re.search("[$,#,@]", n):
        rule = False
    if rule and 6 <= len(n) <= 12:
        legal_password.append(n)
print(','.join(legal_password))
