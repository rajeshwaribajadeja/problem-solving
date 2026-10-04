def start1(a, b):
    """
    Start with 2 int arrays, a and b, of any length.
    Return how many of the arrays have 1 as their first element.

    start1([1, 2, 3], [1, 3]) → 2
    start1([7, 2, 3], [1]) → 1
    start1([1, 2], []) → 1
    """
    return (len(a) > 0 and a[0] == 1) + (len(b) > 0 and b[0] == 1)


print(start1([1, 2, 3], [1, 3]))
print(start1([7, 2, 3], [1]))
print(start1([1, 2], []))
