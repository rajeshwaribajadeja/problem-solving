def str_copies(s, sub, n):
    """
    Given a string and a non-empty substring sub, compute recursively
    if at least n copies of sub appear in the string somewhere,
    possibly with overlapping.


    str_copies("catcowcat", "cat", 2) → True
    str_copies("catcowcat", "cow", 2) → False
    str_copies("catcowcat", "cow", 1) → True
    """

    if n == 0:
        return True

    if len(s) < len(sub):
        return False

    if s[:len(sub)] == sub:
        return str_copies(s[1:], sub, n - 1)

    return str_copies(s[1:], sub, n)


print(str_copies("catcowcat", "cat", 2))
print(str_copies("catcowcat", "cow", 2))
print(str_copies("catcowcat", "cow", 1))
