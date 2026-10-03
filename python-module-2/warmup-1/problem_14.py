def close10(a, b):
    """
    Given 2 int values, return whichever value is nearest to the value 10, or return 0 in the event of a tie.


    close10(8, 13) → 8
    close10(13, 8) → 8
    close10(13, 7) → 0
    """

    if abs(10-a) == abs(10-b):
        return 0

    elif abs(10-a) < abs(10-b):
        return a

    else:
        return b

print(close10(8, 13))
print(close10(13, 8))
print(close10(13, 7))