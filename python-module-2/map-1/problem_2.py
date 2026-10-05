def map_share(map):
    """
    Modify and return the given map as follows: if the key "a" has a value,
    set the key "b" to have that same value. In all cases remove the key "c",
    leaving the rest of the map unchanged.


    map_share({"a": "aaa", "b": "bbb", "c": "ccc"}) → {"a": "aaa", "b": "aaa"}
    map_share({"b": "xyz", "c": "ccc"}) → {"b": "xyz"}
    map_share({"a": "aaa", "c": "meh", "d": "hi"}) → {"a": "aaa", "b": "aaa", "d": "hi"}
    """

    if "a" in map:
        map["b"] = map["a"]

    map.pop("c", None)

    return map


print(map_share({"a": "aaa", "b": "bbb", "c": "ccc"}))
print(map_share({"b": "xyz", "c": "ccc"}))
print(map_share({"a": "aaa", "c": "meh", "d": "hi"}))