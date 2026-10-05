def map_ab(map):
    """
    Modify and return the given map as follows: for this problem the map may
    or may not contain the "a" and "b" keys. If both keys are present, append
    their 2 string values together and store the result under the key "ab".


    map_ab({"a": "Hi", "b": "There"}) → {"a": "Hi", "ab": "HiThere", "b": "There"}
    map_ab({"a": "Hi"}) → {"a": "Hi"}
    map_ab({"b": "There"}) → {"b": "There"}
    """

    if "a" in map and "b" in map:
        map["ab"] = map["a"] + map["b"]

    return map


print(map_ab({"a": "Hi", "b": "There"}))
print(map_ab({"a": "Hi"}))
print(map_ab({"b": "There"}))