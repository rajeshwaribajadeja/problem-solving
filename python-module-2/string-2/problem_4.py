def repeat_end(str, n):
    """
    Given a string and an int n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between 0 and the length of the string, inclusive.

    repeat_end("Hello", 3) → "llollollo"
    repeat_end("Hello", 2) → "lolo"
    repeat_end("Hello", 1) → "o"

    """
    return str[-n:] * n

print(repeat_end("Hello", 3))
print(repeat_end("Hello", 2))
print(repeat_end("Hello", 1))
