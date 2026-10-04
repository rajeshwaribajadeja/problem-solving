def mix_string(a, b):
    """
    Given two strings, a and b, create a bigger string made of the first char of a, the first char of b, the second char of a, the second char of b, and so on. Any leftover chars go at the end of the result.


    mix_string("abc", "xyz") → "axbycz"
    mix_string("Hi", "There") → "HTihere"
    mix_string("xxxx", "There") → "xTxhxexre"
    """

    result = ""
    length = min(len(a), len(b))

    for i in range(length):
        result += a[i] + b[i]

    result += a[length:]
    result += b[length:]

    return result

print(mix_string("abc", "xyz"))
print(mix_string("Hi", "There"))
print(mix_string("xxxx", "There"))


