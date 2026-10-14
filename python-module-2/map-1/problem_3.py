"""Map-1: map_ab problem solution."""


def map_ab(map_dict: dict) -> dict:
    """Modify map: if both 'a' and 'b' are present, store concatenation in 'ab'.

    Args:
        map_dict: Input dictionary with string keys and string values.

    Returns:
        The modified dictionary.

    Complexity:
        Time Complexity: O(La + Lb) where La and Lb are the lengths of the
            string values for keys 'a' and 'b'.
        Space Complexity: O(La + Lb) auxiliary space for the concatenated
            string.

    Examples:
        >>> map_ab({"a": "Hi", "b": "There"})
        {'a': 'Hi', 'b': 'There', 'ab': 'HiThere'}
        >>> map_ab({"a": "Hi"})
        {'a': 'Hi'}
        >>> map_ab({"b": "There"})
        {'b': 'There'}
    """
    if "a" in map_dict and "b" in map_dict:
        map_dict["ab"] = map_dict["a"] + map_dict["b"]
    return map_dict


if __name__ == "__main__":
    print(map_ab({"a": "Hi", "b": "There"}))
    print(map_ab({"a": "Hi"}))
    print(map_ab({"b": "There"}))