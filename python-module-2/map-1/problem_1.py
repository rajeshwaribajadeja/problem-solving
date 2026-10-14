"""Map-1: map_bully problem solution."""


def map_bully(map_dict: dict) -> dict:
    """Modify map: if 'a' has a value, set 'b' to that value and 'a' to ''.

    Basically 'b' is a bully, taking the value of 'a' and replacing it
    with the empty string.

    Args:
        map_dict: Input dictionary with string keys and string values.

    Returns:
        The modified dictionary.

    Complexity:
        Time Complexity: O(1) assuming small strings, or O(L) where L is
            the length of the string value for key 'a'.
        Space Complexity: O(1) auxiliary space (modified in-place).

    Examples:
        >>> map_bully({"a": "candy", "b": "dirt"})
        {'a': '', 'b': 'candy'}
        >>> map_bully({"a": "candy"})
        {'a': '', 'b': 'candy'}
        >>> map_bully({"a": "candy", "b": "carrot", "c": "meh"})
        {'a': '', 'b': 'candy', 'c': 'meh'}
    """
    if "a" in map_dict:
        map_dict["b"] = map_dict["a"]
        map_dict["a"] = ""
    return map_dict


if __name__ == "__main__":
    print(map_bully({"a": "candy", "b": "dirt"}))
    print(map_bully({"a": "candy"}))
    print(map_bully({"a": "candy", "b": "carrot", "c": "meh"}))