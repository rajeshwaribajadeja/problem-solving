def bigger_two(a, b):
    """
    Start with 2 int arrays, a and b, each length 2.
    Consider the sum of the values in each array.
    Return the array which has the largest sum.
    In event of a tie, return a.

    bigger_two([1, 2], [3, 4]) → [3, 4]
    bigger_two([3, 4], [1, 2]) → [3, 4]
    bigger_two([1, 1], [1, 2]) → [1, 2]
    """

    return a if a[0] + a[1] > b[0] + b[1] else b

    # if sum(a) >= sum(b):
    #     return a
    # else:
    #     return b


print(bigger_two([1, 2], [3, 4]))
print(bigger_two([3, 4], [1, 2]))
print(bigger_two([1, 1], [1, 2]))
