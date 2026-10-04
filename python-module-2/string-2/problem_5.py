def repeat_front(str, n):
    """
    Given a string and an int n, return a string made of the first n characters of the string, followed by the first n-1 characters of the string, and so on. You may assume that n is between 0 and the length of the string, inclusive (i.e. n >= 0 and n <= str.length()).


    repeatFront("Chocolate", 4) → "ChocChoChC"
    repeatFront("Chocolate", 3) → "ChoChC"
    repeatFront("Ice Cream", 2) → "IcI"

    """
    result = ""
    i = n

    while i >= 0:
        result += str[:i]
        i -= 1

    # for i in range(n, 0, -1):
    #     result += str[:i]

    return result

print(repeat_front("Chocolate", 4))
print(repeat_front("Chocolate", 3))
print(repeat_front("Ice Cream", 2))
