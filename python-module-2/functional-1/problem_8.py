def lower(words):
    """
    Given a list of strings, return a list where each string
    is converted to lower case.


    lower(["Hello", "Hi"]) → ["hello", "hi"]
    lower(["AAA", "BBB", "ccc"]) → ["aaa", "bbb", "ccc"]
    lower(["KitteN", "ChocolaTE"]) → ["kitten", "chocolate"]
    """

    return list(map(lambda x: x.lower(), words))


print(lower(["Hello", "Hi"]))
print(lower(["AAA", "BBB", "ccc"]))
print(lower(["KitteN", "ChocolaTE"]))
