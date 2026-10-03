def back_around(str):
    """
    Given a string, take the last char and return a new string with the last char added at the front and back, so "cat" yields "tcatt". The original string will be length 1 or more.


    back_around("cat") → "tcatt"
    back_around("Hello") → "oHelloo"
    back_around("a") → "aaa"

    """
    return str[-1] + str + str[-1]

print(back_around("cat"))
print(back_around("Hello"))
print(back_around("a"))