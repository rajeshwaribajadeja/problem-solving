"""Map-1: map_ab_4 problem solution."""


def map_ab_4(map_dict: dict) -> dict:
    """Modify map: store longer of 'a'/'b' into 'c'; clear both if equal
    length.

    Args:
        map_dict: Input dictionary with string keys and string values.

    Returns:
        The modified dictionary.

    Complexity:
        Time Complexity: O(1) assuming small strings, or O(L) where L is
            the length of the longer string.
        Space Complexity: O(1) auxiliary space (modified in-place).

    Examples:
        >>> map_ab_4({"a": "aaa", "b": "bb", "c": "cake"})
        {'a': 'aaa', 'b': 'bb', 'c': 'aaa'}
        >>> map_ab_4({"a": "aa", "b": "bbb", "c": "cake"})
        {'a': 'aa', 'b': 'bbb', 'c': 'bbb'}
        >>> map_ab_4({"a": "aa", "b": "bbb"})
        {'a': 'aa', 'b': 'bbb', 'c': 'bbb'}
    """
    if "a" in map_dict and "b" in map_dict:
        len_a = len(map_dict["a"])
        len_b = len(map_dict["b"])
        if len_a > len_b:
            map_dict["c"] = map_dict["a"]
        elif len_b > len_a:
            map_dict["c"] = map_dict["b"]
        else:
            map_dict["a"] = ""
            map_dict["b"] = ""
    return map_dict


if __name__ == "__main__":
    print(map_ab_4({"a": "aaa", "b": "bb", "c": "cake"}))
    print(map_ab_4({"a": "aa", "b": "bbb", "c": "cake"}))
    print(map_ab_4({"a": "aa", "b": "bbb"}))