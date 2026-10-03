def int_max(a,b,c):
    """
    Given three int values, a b c, return the largest.


    int_max(1, 2, 3) → 3
    int_max(1, 3, 2) → 3
    int_max(3, 2, 1) → 3
    """

    if a > b:
        if a > c:
            return a
        else:
            return c

    else:
        if b > c:
            return b 

        else:
            return c

    # return max(a,b,c)

print(int_max(1, 2, 3))
print(int_max(1, 3, 2))
print(int_max(3, 2, 1))