def topping_3(map):
    """
    Given a map of food keys and topping values, modify and return the map
    as follows: if the key "potato" has a value, set that as the value for
    the key "fries". If the key "salad" has a value, set that as the value
    for the key "spinach".


    topping_3({"potato": "ketchup"}) → {"potato": "ketchup", "fries": "ketchup"}
    topping_3({"potato": "butter"}) → {"potato": "butter", "fries": "butter"}
    topping_3({"salad": "oil", "potato": "ketchup"}) → {"spinach": "oil", "salad": "oil", "potato": "ketchup", "fries": "ketchup"}
    """

    if map.get("potato"):
        map["fries"] = map.get("potato")

    if map.get("salad"):
        map["spinach"] = map.get("salad")

    return map


print(topping_3({"potato": "ketchup"}))
print(topping_3({"potato": "butter"}))
print(topping_3({"salad": "oil", "potato": "ketchup"}))