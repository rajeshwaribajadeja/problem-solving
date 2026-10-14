"""Map-1: map_ab_3 problem solution."""


def map_ab_3(map_dict: dict) -> dict:
    """Modify map: if exactly one of 'a' or 'b' exists, copy to the
    other.

    Args:
        map_dict: Input dictionary with string keys and string values.

    Returns:
        The modified dictionary.

    Complexity:
        Time Complexity: O(1) assuming small strings, or O(L) to copy
            string value.
        Space Complexity: O(1) auxiliary space (modified in-place).

    Examples:
        >>> map_ab_3({"a": "aaa", "c": "cake"})
        {'a': 'aaa', 'c': 'cake', 'b': 'aaa'}
        >>> map_ab_3({"b": "bbb", "c": "cake"})
        {'b': 'bbb', 'c': 'cake', 'a': 'bbb'}
        >>> map_ab_3({"a": "aaa", "b": "bbb", "c": "cake"})
        {'a': 'aaa', 'b': 'bbb', 'c': 'cake'}
    """
    if "a" in map_dict and "b" not in map_dict:
        map_dict["b"] = map_dict["a"]
    elif "b" in map_dict and "a" not in map_dict:
        map_dict["a"] = map_dict["b"]
    return map_dict


if __name__ == "__main__":
    print(map_ab_3({"a": "aaa", "c": "cake"}))
    print(map_ab_3({"b": "bbb", "c": "cake"}))
    print(map_ab_3({"a": "aaa", "b": "bbb", "c": "cake"}))