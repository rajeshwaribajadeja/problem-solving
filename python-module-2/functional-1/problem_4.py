def copies_3(words):
    """
    Given a list of strings, return a list where each string is
    replaced by 3 copies of the string concatenated together.


    copies_3(["a", "bb", "ccc"]) → ["aaa", "bbbbbb", "ccccccccc"]
    copies_3(["24", "a", ""]) → ["242424", "aaa", ""]
    copies_3(["hello", "there"]) → ["hellohellohello", "theretherethere"]
    """

    return list(map(lambda x: x * 3, words))


print(copies_3(["a", "bb", "ccc"]))
print(copies_3(["24", "a", ""]))
print(copies_3(["hello", "there"]))
