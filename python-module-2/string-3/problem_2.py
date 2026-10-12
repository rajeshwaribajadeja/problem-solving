"""String-3: without_string problem solution."""


def without_string(base: str, remove: str) -> str:
    """Remove all non-overlapping instances of remove from base (case-insensitive).

    Given two strings, base and remove, return a version of the base
    string where all instances of the remove string have been removed
    (not case sensitive). Remove only non-overlapping instances.

    Args:
        base: The source string.
        remove: The target substring to remove.

    Returns:
        The base string with all remove instances stripped.

    Complexity:
        Time Complexity: O(len(base) * len(remove)).
        Space Complexity: O(len(base)) to store the resulting string.

    Examples:
        >>> without_string("Hello there", "llo")
        'He there'
        >>> without_string("Hello there", "e")
        'Hllo thr'
        >>> without_string("Hello there", "x")
        'Hello there'
        >>> without_string("xxx", "xx")
        'x'
    """
    result = []
    i = 0
    rem_len = len(remove)
    rem_lower = remove.lower()

    while i < len(base):
        if i + rem_len <= len(base) and base[i:i + rem_len].lower() == rem_lower:
            i += rem_len
        else:
            result.append(base[i])
            i += 1

    return "".join(result)


if __name__ == "__main__":
    print(without_string("Hello there", "llo"))
    print(without_string("Hello there", "e"))
    print(without_string("Hello there", "x"))
    print(without_string("xxx", "xx"))