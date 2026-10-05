def topping_2(map):
    """
    Given a map of food keys and their topping values, modify and return the
    map as follows: if the key "ice cream" has a value, set that as the value
    for the key "yogurt" also. If the key "spinach" has a value, change that
    value to "nuts".


    topping_2({"ice cream": "cherry"}) → {"yogurt": "cherry", "ice cream": "cherry"}
    topping_2({"spinach": "dirt", "ice cream": "cherry"}) → {"yogurt": "cherry", "spinach": "nuts", "ice cream": "cherry"}
    topping_2({"yogurt": "salt"}) → {"yogurt": "salt"}
    """

    if map.get("ice cream"):
        map["yogurt"] = map.get("ice cream")

    if map.get("spinach"):
        map["spinach"] = "nuts"

    return map


print(topping_2({"ice cream": "cherry"}))
print(topping_2({"spinach": "dirt", "ice cream": "cherry"}))
print(topping_2({"yogurt": "salt"}))