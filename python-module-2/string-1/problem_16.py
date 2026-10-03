def min_cat(a, b):
    """
    Given two strings, append them together (known as "concatenation") and return the result. However, if the strings are different lengths, omit chars from the longer string so it is the same length as the shorter string. So "Hello" and "Hi" yield "loHi". The strings may be any length.


    min_cat("Hello", "Hi") → "loHi"
    min_cat("Hello", "java") → "ellojava"
    min_cat("java", "Hello") → "javaello"
    """

    if len(a) > len(b):
        a = a[-len(b):]
    elif len(b) > len(a):
        b = b[-len(a):]

    return a + b

print(min_cat("Hello", "Hi"))
print(min_cat("Hello", "java"))
print(min_cat("java", "Hello"))
