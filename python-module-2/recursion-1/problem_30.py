def str_dist(s, sub):
    """
    Given a string and a non-empty substring sub, compute recursively
    the largest substring which starts and ends with sub and return
    its length.


    str_dist("catcowcat", "cat") → 9
    str_dist("catcowcat", "cow") → 3
    str_dist("cccatcowcatxx", "cat") → 9
    """

    if not s.startswith(sub):
        return str_dist(s[1:], sub)

    if not s.endswith(sub):
        return str_dist(s[:-1], sub)

    return len(s)


print(str_dist("catcowcat", "cat"))
print(str_dist("catcowcat", "cow"))
print(str_dist("cccatcowcatxx", "cat"))
