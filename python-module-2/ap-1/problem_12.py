"""AP-1: match_up problem solution."""


def match_up(a: list, b: list) -> int:
    """Return count of pairs of non-empty strings starting with the same
    character.

    Given 2 arrays that are the same length containing strings, compare
    the 1st string in one array to the 1st string in the other array, the
    2nd to the 2nd and so on. Count the number of times that the 2 strings
    are non-empty and start with the same char.

    Args:
        a: First list of strings.
        b: Second list of strings of identical length.

    Returns:
        The count of matching non-empty string pairs.

    Complexity:
        Time Complexity: O(N) where N is the length of the lists.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> match_up(["aa", "bb", "cc"], ["aaa", "xx", "bb"])
        1
        >>> match_up(["aa", "bb", "cc"], ["aaa", "b", "bb"])
        2
        >>> match_up(["aa", "bb", "cc"], ["", "", "ccc"])
        1
    """
    count = 0
    for str_a, str_b in zip(a, b):
        if str_a and str_b and str_a[0] == str_b[0]:
            count += 1
    return count


if __name__ == "__main__":
    print(match_up(["aa", "bb", "cc"], ["aaa", "xx", "bb"]))
    print(match_up(["aa", "bb", "cc"], ["aaa", "b", "bb"]))
    print(match_up(["aa", "bb", "cc"], ["", "", "ccc"]))