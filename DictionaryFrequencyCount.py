"""
Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

Hints:
Use dict to store key/value pairs.
Use dict.get() method to lookup a key with default value.
"""


x = input("Enter a string: ")
d = {}
for i in x:
    d[i] = d.get(i, 0) + 1
    # if i in d:
    #     d[i] += 1
    # else:
    #     d[i] = 1
a = sorted(d.keys())
for i in a:
    print(i + ',' + str(d.get(i)))
