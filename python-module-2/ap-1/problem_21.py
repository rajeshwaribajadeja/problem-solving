def common_two(a, b):
    """
    Start with two arrays of strings, a and b, each in alphabetical order, possibly with duplicates. Return the count of the number of strings which appear in both arrays. The best "linear" solution makes a single pass over both arrays, taking advantage of the fact that they are in alphabetical order.

    common_two(["a", "c", "x"], ["b", "c", "d", "x"]) → 2
    common_two(["a", "c", "x"], ["a", "b", "c", "x", "z"]) → 3
    common_two(["a", "b", "c"], ["a", "b", "c"]) → 3
    """

    i = 0
    j = 0
    count = 0

    while i < len(a) and j < len(b):

        if a[i] == b[j]:
            count += 1
            i += 1
            j += 1

        elif a[i] < b[j]:
            i += 1

        else:
            j += 1

    return count


print(common_two(["a", "c", "x"], ["b", "c", "d", "x"]))
print(common_two(["a", "c", "x"], ["a", "b", "c", "x", "z"]))
print(common_two(["a", "b", "c"], ["a", "b", "c"]))