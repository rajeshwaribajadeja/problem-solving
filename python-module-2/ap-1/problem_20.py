def merge_two(a, b, n):
    """
    Start with two arrays of strings, A and B, each with its elements in alphabetical order and without duplicates. Return a new array containing the first N elements from the two arrays. The result array should be in alphabetical order and without duplicates. A and B will both have a length which is N or more. The best "linear" solution makes a single pass over A and B, taking advantage of the fact that they are in alphabetical order, copying elements directly to the new array.

    merge_two(["a", "c", "z"], ["b", "f", "z"], 3) → ["a", "b", "c"]
    merge_two(["a", "c", "z"], ["c", "f", "z"], 3) → ["a", "c", "f"]
    merge_two(["f", "g", "z"], ["c", "f", "g"], 3) → ["c", "f", "g"]
    """

    result = []
    i = 0
    j = 0

    while len(result) < n:
        if a[i] < b[j]:
            value = a[i]
            i += 1
        elif b[j] < a[i]:
            value = b[j]
            j += 1
        else:
            value = a[i]
            i += 1
            j += 1

        result.append(value)

    return result


print(merge_two(["a", "c", "z"], ["b", "f", "z"], 3))
print(merge_two(["a", "c", "z"], ["c", "f", "z"], 3))
print(merge_two(["f", "g", "z"], ["c", "f", "g"], 3))