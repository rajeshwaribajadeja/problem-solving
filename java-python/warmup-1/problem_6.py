def icy_hot(temp1, temp2):
    """
    Given two temperatures, return true if one is less than 0 and the other is greater than 100.


    icy_hot(120, -1) → true
    icy_hot(-1, 120) → true
    icy_hot(2, 120) → false

    """

    return (temp1 < 0 and temp2 > 100) or (temp1 > 100 and temp2 < 0)

print(icy_hot(120, -1))
print(icy_hot(-1, 120))
print(icy_hot(2, 120))