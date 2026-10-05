def map_ab_3(map):
    """
    Modify and return the given map as follows: if exactly one of the keys
    "a" or "b" has a value in the map (but not both), set the other to have
    that same value in the map.


    map_ab_3({"a": "aaa", "c": "cake"}) → {"a": "aaa", "b": "aaa", "c": "cake"}
    map_ab_3({"b": "bbb", "c": "cake"}) → {"a": "bbb", "b": "bbb", "c": "cake"}
    map_ab_3({"a": "aaa", "b": "bbb", "c": "cake"}) → {"a": "aaa", "b": "bbb", "c": "cake"}
    """

    if map.get("a") and not map.get("b"):
        map["b"] = map.get("a")

    elif map.get("b") and not map.get("a"):
        map["a"] = map.get("b")

    return map


print(map_ab_3({"a": "aaa", "c": "cake"}))
print(map_ab_3({"b": "bbb", "c": "cake"}))
print(map_ab_3({"a": "aaa", "b": "bbb", "c": "cake"}))