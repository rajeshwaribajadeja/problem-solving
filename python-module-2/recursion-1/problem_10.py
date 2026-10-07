def count_x(s):
    """
    Given a string, compute recursively the number of lowercase 'x'
    characters in the string.


    count_x("xxhixx") → 4
    count_x("xhixhix") → 3
    count_x("hi") → 0
    """

    if s == "":
        return 0

    # if s[0] == "x":
    #     return 1 + count_x(s[1:])

    return 1 + count_x(s[1:]) if s[0] == "x" else count_x(s[1:])


print(count_x("xxhixx"))
print(count_x("xhixhix"))
print(count_x("hi"))
