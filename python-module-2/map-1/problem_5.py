"""Map-1: topping_2 problem solution."""


def topping_2(map_dict: dict) -> dict:
    """Modify map: copy 'ice cream' to 'yogurt'; change 'spinach' to 'nuts'.

    If the key 'ice cream' has a value, set that as the value for the
    key 'yogurt' also. If the key 'spinach' has a value, change that
    value to 'nuts'.

    Args:
        map_dict: Input dictionary with food keys and topping values.

    Returns:
        The modified dictionary.

    Complexity:
        Time Complexity: O(1) average time for dictionary lookups and
            updates.
        Space Complexity: O(1) auxiliary space (modified in-place).

    Examples:
        >>> topping_2({"ice cream": "cherry"})
        {'ice cream': 'cherry', 'yogurt': 'cherry'}
        >>> topping_2({"spinach": "dirt", "ice cream": "cherry"})
        {'spinach': 'nuts', 'ice cream': 'cherry', 'yogurt': 'cherry'}
        >>> topping_2({"yogurt": "salt"})
        {'yogurt': 'salt'}
    """
    if map_dict.get("ice cream"):
        map_dict["yogurt"] = map_dict["ice cream"]
    if map_dict.get("spinach"):
        map_dict["spinach"] = "nuts"
    return map_dict


if __name__ == "__main__":
    print(topping_2({"ice cream": "cherry"}))
    print(topping_2({"spinach": "dirt", "ice cream": "cherry"}))
    print(topping_2({"yogurt": "salt"}))