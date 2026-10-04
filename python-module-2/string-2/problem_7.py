def prefix_again(str, n):
    """
    Given a string, consider the prefix string made of the first N chars of the string. Does that prefix string appear somewhere else in the string? Assume that the string is not empty and that N is in the range 1..str.length().

    prefix_again("abXYabc", 1) → true
    prefix_again("abXYabc", 2) → true
    prefix_again("abXYabc", 3) → false
    """
    return str[:n] in str[n:]

print(prefix_again("abXYabc", 1))
print(prefix_again("abXYabc", 2))
print(prefix_again("abXYabc", 3))