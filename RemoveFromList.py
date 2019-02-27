"""
By using list comprehension, please write a program to print the list after removing the value 24 in
[12,24,35,24,88,120,155].

Hints:
Use list's remove method to delete a value.
"""

x = [12, 24, 35, 24, 88, 120, 155]
while 24 in x:
    x.remove(24)
print(x)


