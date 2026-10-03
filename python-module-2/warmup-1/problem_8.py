def has_teen(a, b, c):
    """
    We'll say that a number is "teen" if it is in the range 13..19 inclusive. Given 3 int values, return true if 1 or more of them are teen.


    has_teen(13, 20, 10) → true
    has_teen(20, 19, 10) → true
    has_teen(20, 10, 21) → true
    """
    return 13 <= a <=19 or 13 <= b <=19 or 13 <= c <=19

print(has_teen(13, 20, 10))
print(has_teen(20, 19, 10))
print(has_teen(20, 10, 21))