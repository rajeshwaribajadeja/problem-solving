def topping_1(map):
    """
    Given a map of food keys and topping values, modify and return the map
    as follows: if the key "ice cream" is present, set its value to "cherry".
    In all cases, set the key "bread" to have the value "butter".


    topping_1({"ice cream": "peanuts"}) → {"bread": "butter", "ice cream": "cherry"}
    topping_1({}) → {"bread": "butter"}
    topping_1({"pancake": "syrup"}) → {"bread": "butter", "pancake": "syrup"}
    """

    if "ice cream" in map:
        map["ice cream"] = "cherry"

    map["bread"] = "butter"

    return map


print(topping_1({"ice cream": "peanuts"}))
print(topping_1({}))
print(topping_1({"pancake": "syrup"}))