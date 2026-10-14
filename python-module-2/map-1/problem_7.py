"""Map-1: map_ab_2 problem solution."""


def map_ab_2(map_dict: dict) -> dict:
    """Modify map: if 'a' and 'b' have equal values, remove them both.

    Args:
        map_dict: Input dictionary with string keys and string values.

    Returns:
        The modified dictionary.

    Complexity:
        Time Complexity: O(1) assuming small strings, or O(L) to compare
            string values of 'a' and 'b'.
        Space Complexity: O(1) auxiliary space (modified in-place).

    Examples:
        >>> map_ab_2({"a": "aaa", "b": "aaa", "c": "cake"})
        {'c': 'cake'}
        >>> map_ab_2({"a": "aaa", "b": "bbb"})
        {'a': 'aaa', 'b': 'bbb'}
        >>> map_ab_2({"a": "aaa", "b": "bbb", "c": "aaa"})
        {'a': 'aaa', 'b': 'bbb', 'c': 'aaa'}
    """
    if "a" in map_dict and "b" in map_dict:
        if map_dict["a"] == map_dict["b"]:
            map_dict.pop("a", None)
            map_dict.pop("b", None)
    return map_dict


if __name__ == "__main__":
    print(map_ab_2({"a": "aaa", "b": "aaa", "c": "cake"}))
    print(map_ab_2({"a": "aaa", "b": "bbb"}))
    print(map_ab_2({"a": "aaa", "b": "bbb", "c": "aaa"}))