def add_star(words):
    """
    Given a list of strings, return a list where each string
    has "*" added at its end.


    add_star(["a", "bb", "ccc"]) → ["a*", "bb*", "ccc*"]
    add_star(["hello", "there"]) → ["hello*", "there*"]
    add_star(["*"]) → ["**"]
    """

    return list(map(lambda x: x + "*", words))


print(add_star(["a", "bb", "ccc"]))
print(add_star(["hello", "there"]))
print(add_star(["*"]))
