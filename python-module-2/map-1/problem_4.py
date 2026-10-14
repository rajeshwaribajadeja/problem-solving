"""Map-1: topping_1 problem solution."""


def topping_1(map_dict: dict) -> dict:
    """Modify map: set 'ice cream' to 'cherry' if present, and 'bread' to
    'butter'.

    Args:
        map_dict: Input dictionary with food keys and topping values.

    Returns:
        The modified dictionary.

    Complexity:
        Time Complexity: O(1) average time for hash map lookups.
        Space Complexity: O(1) auxiliary space (modified in-place).

    Examples:
        >>> topping_1({"ice cream": "peanuts"})
        {'ice cream': 'cherry', 'bread': 'butter'}
        >>> topping_1({})
        {'bread': 'butter'}
        >>> topping_1({"pancake": "syrup"})
        {'pancake': 'syrup', 'bread': 'butter'}
    """
    if "ice cream" in map_dict:
        map_dict["ice cream"] = "cherry"
    map_dict["bread"] = "butter"
    return map_dict


if __name__ == "__main__":
    print(topping_1({"ice cream": "peanuts"}))
    print(topping_1({}))
    print(topping_1({"pancake": "syrup"}))