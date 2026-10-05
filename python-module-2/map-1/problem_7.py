def map_ab_2(map):
    """
    Modify and return the given map as follows: if the keys "a" and "b"
    are both in the map and have equal values, remove them both.


    map_ab_2({"a": "aaa", "b": "aaa", "c": "cake"}) → {"c": "cake"}
    map_ab_2({"a": "aaa", "b": "bbb"}) → {"a": "aaa", "b": "bbb"}
    map_ab_2({"a": "aaa", "b": "bbb", "c": "aaa"}) → {"a": "aaa", "b": "bbb", "c": "aaa"}
    """

    if "a" in map and "b" in map and map.get("a") == map.get("b"):
        map.pop("a")
        map.pop("b")

    return map


print(map_ab_2({"a": "aaa", "b": "aaa", "c": "cake"}))
print(map_ab_2({"a": "aaa", "b": "bbb"}))
print(map_ab_2({"a": "aaa", "b": "bbb", "c": "aaa"}))