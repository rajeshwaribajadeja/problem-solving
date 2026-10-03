def start_word(str, word):
    """
    Given a string and a second "word" string, we'll say that the word matches the string if it appears at the front of the string, except its first char does not need to match exactly. On a match, return the front of the string, or otherwise return the empty string. So, so with the string "hippo" the word "hi" returns "hi" and "xip" returns "hip". The word will be at least length 1.


    start_word("hippo", "hi") → "hi"
    start_word("hippo", "xip") → "hip"
    start_word("hippo", "i") → "h"
    """
    if len(str) < len(word):
        return ""

    if str[1:len(word)] == word[1:]:
        return str[:len(word)]

    return ""

print(start_word("hippo", "hi"))
print(start_word("hippo", "xip"))
print(start_word("hippo", "i"))