def divides_self(n):
    """
    We'll say that a positive int divides itself if every digit in the number divides into the number evenly. So for example 128 divides itself since 1, 2, and 8 all divide into 128 evenly. We'll say that 0 does not divide into anything evenly, so no number with a 0 digit divides itself. Note: use % to get the rightmost digit, and / to discard the rightmost digit.


    divides_self(128) → True
    divides_self(12) → True
    divides_self(120) → False
    """

    original = n

    while n > 0:
        digit = n % 10

        if digit == 0 or original % digit != 0:
            return False

        n = n // 10

    return True


print(divides_self(128))
print(divides_self(12))
print(divides_self(120))