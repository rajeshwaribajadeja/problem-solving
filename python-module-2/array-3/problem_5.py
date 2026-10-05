def linear_in(outer, inner):
    """
    Given two arrays of ints sorted in increasing order, outer and inner, return true if all of the numbers in inner appear in outer. The best solution makes only a single "linear" pass of both arrays, taking advantage of the fact that both arrays are already in sorted order.

    linear_in([1, 2, 4, 6], [2, 4]) → True
    linear_in([1, 2, 4, 6], [2, 3, 4]) → False
    linear_in([1, 2, 4, 4, 6], [2, 4]) → True
    """

    i = 0
    j = 0

    while i < len(outer) and j < len(inner):
        if outer[i] == inner[j]:
            i += 1
            j += 1
        elif outer[i] < inner[j]:
            i += 1
        else:
            return False

    return j == len(inner)

    


print(linear_in([1, 2, 4, 6], [2, 4]))
print(linear_in([1, 2, 4, 6], [2, 3, 4]))
print(linear_in([1, 2, 4, 4, 6], [2, 4]))
