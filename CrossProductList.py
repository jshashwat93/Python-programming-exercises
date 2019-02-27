"""
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and
the object is in ["Hockey","Football"].

Hints:
Use list[index] notation to get a element from a list.
"""

x1 = ["I", "You"]
x2 = ["Play", "Love"]
x3 = ["Hockey","Football"]
for i in range(len(x1)):
    for j in range(len(x2)):
        for k in range(len(x3)):
            print(x1[i], x2[j], x3[k])


"""
By using list comprehension, please write a program to print the list after removing delete numbers which are divisible
by 5 and 7 in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list."""