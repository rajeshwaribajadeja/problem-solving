def mirror_ends(str):
    """
    Given a string, look for a mirror image (backwards) string at both
    the beginning and end of the given string.

    mirror_ends("abXYZba") → "ab"
    mirror_ends("abca") → "a"
    mirror_ends("aba") → "aba"
    """

    result = ""
    rev_str = str[::-1]
    for i in range(len(str)):
        if str[i] == rev_str[i]:
            result += str[i]

        else:
            break

    return result

    # result = ""

    # for i in range(1, len(str) + 1):
    #     if str[:i] == str[-i:][::-1]:
    #         result = str[:i]

    # return result


print(mirror_ends("abXYZba"))
print(mirror_ends("abca"))
print(mirror_ends("aba"))
