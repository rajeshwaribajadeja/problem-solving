def map_ab_4(map):
    """
    Modify and return the given map as follows: if the keys "a" and "b"
    have values that have different lengths, then set "c" to have the
    longer value. If the values exist and have the same length, change
    them both to the empty string in the map.


    map_ab_4({"a": "aaa", "b": "bb", "c": "cake"}) → {"a": "aaa", "b": "bb", "c": "aaa"}
    map_ab_4({"a": "aa", "b": "bbb", "c": "cake"}) → {"a": "aa", "b": "bbb", "c": "bbb"}
    map_ab_4({"a": "aa", "b": "bbb"}) → {"a": "aa", "b": "bbb", "c": "bbb"}
    """

    if map.get("a") and map.get("b"):
        if len(map.get("a")) > len(map.get("b")):
            map["c"] = map.get("a")

        elif len(map.get("b")) > len(map.get("a")):
            map["c"] = map.get("b")

        else:
            map["a"] = ""
            map["b"] = ""

    return map


print(map_ab_4({"a": "aaa", "b": "bb", "c": "cake"}))
print(map_ab_4({"a": "aa", "b": "bbb", "c": "cake"}))
print(map_ab_4({"a": "aa", "b": "bbb"}))