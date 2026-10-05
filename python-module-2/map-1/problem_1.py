def map_bully(map):
    """
    Modify and return the given map as follows: if the key "a" has a value,
    set the key "b" to have that value, and set the key "a" to have the
    value "". Basically "b" is a bully, taking the value and replacing it
    with the empty string.


    map_bully({"a": "candy", "b": "dirt"}) → {"a": "", "b": "candy"}
    map_bully({"a": "candy"}) → {"a": "", "b": "candy"}
    map_bully({"a": "candy", "b": "carrot", "c": "meh"}) → {"a": "", "b": "candy", "c": "meh"}
    """

    if "a" in map:
        map["b"] = map["a"]
        map["a"] = ""

    return map


print(map_bully({"a": "candy", "b": "dirt"}))
print(map_bully({"a": "candy"}))
print(map_bully({"a": "candy", "b": "carrot", "c": "meh"}))