"""AP-1: merge_two problem solution."""


def merge_two(a: list, b: list, n: int) -> list:
    """Return the first n alphabetical strings from two sorted
    duplicate-free arrays.

    Start with two arrays of strings, a and b, each in alphabetical order
    and without duplicates. Return a new array containing the first n
    elements from the two arrays in alphabetical order without duplicates.

    Args:
        a: First sorted list of unique strings.
        b: Second sorted list of unique strings.
        n: The number of elements to produce.

    Returns:
        A list of length n with merged elements in alphabetical order.

    Complexity:
        Time Complexity: O(n)
        Space Complexity: O(n) for the output list.

    Examples:
        >>> merge_two(["a", "c", "z"], ["b", "f", "z"], 3)
        ['a', 'b', 'c']
        >>> merge_two(["a", "c", "z"], ["c", "f", "z"], 3)
        ['a', 'c', 'f']
        >>> merge_two(["f", "g", "z"], ["c", "f", "g"], 3)
        ['c', 'f', 'g']
    """
    result = []
    i = 0
    j = 0

    while len(result) < n:
        if a[i] < b[j]:
            val = a[i]
            i += 1
        elif b[j] < a[i]:
            val = b[j]
            j += 1
        else:
            val = a[i]
            i += 1
            j += 1
        result.append(val)

    return result


if __name__ == "__main__":
    print(merge_two(["a", "c", "z"], ["b", "f", "z"], 3))
    print(merge_two(["a", "c", "z"], ["c", "f", "z"], 3))
    print(merge_two(["f", "g", "z"], ["c", "f", "g"], 3))