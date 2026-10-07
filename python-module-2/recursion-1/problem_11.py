def count_hi(s):
    """
    Given a string, compute recursively the number of times
    lowercase "hi" appears in the string.


    count_hi("xxhixx") → 1
    count_hi("xhixhix") → 2
    count_hi("hi") → 1
    """

    if len(s) < 2:
        return 0

    # if s[0:2] == "hi":
    #     return 1 + count_hi(s[2:])

    return 1 + count_hi(s[2:]) if s[0:2] == "hi" else count_hi(s[1:])


print(count_hi("xxhixx"))
print(count_hi("xhixhix"))
print(count_hi("hi"))
