"""Map-1: map_share problem solution."""


def map_share(map_dict: dict) -> dict:
    """Modify map: if 'a' has a value, set 'b' to that value; remove 'c'.

    Args:
        map_dict: Input dictionary with string keys and string values.

    Returns:
        The modified dictionary.

    Complexity:
        Time Complexity: O(1) assuming small strings, or O(L) where L is
            the length of the string value for key 'a'.
        Space Complexity: O(1) auxiliary space (modified in-place).

    Examples:
        >>> map_share({"a": "aaa", "b": "bbb", "c": "ccc"})
        {'a': 'aaa', 'b': 'aaa'}
        >>> map_share({"b": "xyz", "c": "ccc"})
        {'b': 'xyz'}
        >>> map_share({"a": "aaa", "c": "meh", "d": "hi"})
        {'a': 'aaa', 'd': 'hi', 'b': 'aaa'}
    """
    if "a" in map_dict:
        map_dict["b"] = map_dict["a"]
    map_dict.pop("c", None)
    return map_dict


if __name__ == "__main__":
    print(map_share({"a": "aaa", "b": "bbb", "c": "ccc"}))
    print(map_share({"b": "xyz", "c": "ccc"}))
    print(map_share({"a": "aaa", "c": "meh", "d": "hi"}))