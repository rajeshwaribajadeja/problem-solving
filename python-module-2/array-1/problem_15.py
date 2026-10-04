def front11(a, b):
    """
    Given 2 int arrays, a and b, of any length, return a new array
    with the first element of each array. If either array is length 0,
    ignore that array.

    front11([1, 2, 3], [7, 9, 8]) → [1, 7]
    front11([1], [2]) → [1, 2]
    front11([1, 7], []) → [1]
    """

    return a[:1] + b[:1]


print(front11([1, 2, 3], [7, 9, 8]))
print(front11([1], [2]))
print(front11([1, 7], []))
