def string_clean(s):
    """
    Given a string, return recursively a "cleaned" string where
    adjacent chars that are the same have been reduced to a single char.


    string_clean("yyzzza") → "yza"
    string_clean("abbbcdd") → "abcd"
    string_clean("Hello") → "Helo"
    """

    if len(s) <= 1:
        return s

    # if s[0] == s[1]:
    #     return string_clean(s[1:])

    return string_clean(s[1:]) if s[0] == s[1] else s[0] + string_clean(s[1:])


print(string_clean("yyzzza"))
print(string_clean("abbbcdd"))
print(string_clean("Hello"))
