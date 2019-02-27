"""
Please write a binary search function which searches an item in a sorted list. The function should return the index of
element to be searched in the list.


Hints:
Use if/elif to deal with conditions.
"""


def binary_search_iterative(n, t):
    beg = 0
    end = len(n) - 1
    while beg <= end:
        mid = beg + ((end - beg) // 2)
        if n[mid] == t:
            return True
        elif n[mid] > t:
            end = mid - 1
        elif n[mid] < t:
            beg = mid + 1
    return False


def binary_search_recursive(n, t, beg, end):
    mid = beg + ((end - beg) // 2)
    if beg > end:
        return False
    elif n[mid] == t:
        return True
    elif n[mid] > t:
        return binary_search_recursive(n, t, beg, mid - 1)
    elif n[mid] < t:
        return binary_search_recursive(n, t, mid + 1, end)


if __name__ == '__main__':
    x = [2, 5, 7, 9, 11, 17, 222]
    y = 11
    print(binary_search_iterative(x, y))
    print(binary_search_recursive(x, y, 0, len(x) - 1))

