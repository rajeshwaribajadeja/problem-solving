"""String-3: not_replace problem solution."""


def not_replace(s: str) -> str:
    """Replace standalone occurrences of "is" with "is not".

    Given a string, return a string where every appearance of the lowercase
    word "is" has been replaced with "is not".

    Args:
        s: The input string.

    Returns:
        String with standalone instances of "is" replaced.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) auxiliary space to construct the result string.

    Examples:
        >>> not_replace("is test")
        'is not test'
        >>> not_replace("is-is")
        'is not-is not'
        >>> not_replace("This is right")
        'This is not right'
    """
    result = []
    i = 0
    n = len(s)

    while i < n:
        if (
            s[i:i + 2] == "is"
            and (i == 0 or not s[i - 1].isalpha())
            and (i + 2 == n or not s[i + 2].isalpha())
        ):
            result.append("is not")
            i += 2
        else:
            result.append(s[i])
            i += 1

    return "".join(result)


if __name__ == "__main__":
    print(not_replace("is test"))
    print(not_replace("is-is"))
    print(not_replace("This is right"))