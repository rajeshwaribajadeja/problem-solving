def concat(a, b):
    """
    Given two strings, append them together (known as "concatenation") and return the result. However, if the concatenation creates a double-char, then omit one of the chars, so "abc" and "cat" yields "abcat".


    concat("abc", "cat") → "abcat"
    concat("dog", "cat") → "dogcat"
    concat("abc", "") → "abc"
    """

    if a and b and a[-1] == b[0]:
        return a + b[1:]
    
    return a + b 

print(concat("abc", "cat"))
print(concat("dog", "cat"))
print(concat("abc", ""))