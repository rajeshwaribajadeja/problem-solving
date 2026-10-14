"""Map-1: topping_3 problem solution."""


def topping_3(map_dict: dict) -> dict:
    """Modify map: copy 'potato' to 'fries'; copy 'salad' to 'spinach'.

    If the key 'potato' has a value, set that as the value for the key
    'fries'. If the key 'salad' has a value, set that as the value for
    the key 'spinach'.

    Args:
        map_dict: Input dictionary with food keys and topping values.

    Returns:
        The modified dictionary.

    Complexity:
        Time Complexity: O(1) average time for dictionary lookups and
            updates.
        Space Complexity: O(1) auxiliary space (modified in-place).

    Examples:
        >>> topping_3({"potato": "ketchup"})
        {'potato': 'ketchup', 'fries': 'ketchup'}
        >>> topping_3({"potato": "butter"})
        {'potato': 'butter', 'fries': 'butter'}
        >>> res = topping_3({"salad": "oil", "potato": "ketchup"})
        >>> res == {
        ...     "salad": "oil", "potato": "ketchup",
        ...     "fries": "ketchup", "spinach": "oil"
        ... }
        True
    """
    if map_dict.get("potato"):
        map_dict["fries"] = map_dict["potato"]
    if map_dict.get("salad"):
        map_dict["spinach"] = map_dict["salad"]
    return map_dict


if __name__ == "__main__":
    print(topping_3({"potato": "ketchup"}))
    print(topping_3({"potato": "butter"}))
    print(topping_3({"salad": "oil", "potato": "ketchup"}))