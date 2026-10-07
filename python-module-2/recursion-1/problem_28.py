def str_count(s, sub):
    """
    Given a string and a non-empty substring sub, compute recursively the number of times that sub appears in the string, without the sub strings overlapping.


    str_count("catcowcat", "cat") → 2
    str_count("catcowcat", "cow") → 1
    str_count("catcowcat", "dog") → 0
    """

    if len(s) < len(sub):
        return 0

    if s[:len(sub)] == sub:
        return 1 + str_count(s[len(sub):], sub)

    return str_count(s[1:], sub)


print(str_count("catcowcat", "cat"))
print(str_count("catcowcat", "cow"))
print(str_count("catcowcat", "dog"))
