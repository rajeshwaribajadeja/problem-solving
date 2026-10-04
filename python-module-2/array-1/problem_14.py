def make2(a, b):
    """
    Given 2 int arrays, a and b, return a new array length 2 containing,
    as much as will fit, the elements from a followed by the elements from b.

    make2([4, 5], [1, 2, 3]) → [4, 5]
    make2([4], [1, 2, 3]) → [4, 1]
    make2([], [1, 2]) → [1, 2]
    """

    # result = a[:2]

    # if len(result) < 2:
    #     result += b[:2 - len(result)]

    # return result

    return (a + b)[:2]


print(make2([4, 5], [1, 2, 3]))
print(make2([4], [1, 2, 3]))
print(make2([], [1, 2]))
