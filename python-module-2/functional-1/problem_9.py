def no_x(words):
    """
    Given a list of strings, return a list where each string
    has all its "x" removed.


    no_x(["ax", "bb", "cx"]) → ["a", "bb", "c"]
    no_x(["xxax", "xbxbx", "xxcx"]) → ["a", "bb", "c"]
    no_x(["x"]) → [""]
    """

    return list(map(lambda x: x.replace("x", ""), words))


print(no_x(["ax", "bb", "cx"]))
print(no_x(["xxax", "xbxbx", "xxcx"]))
print(no_x(["x"]))
