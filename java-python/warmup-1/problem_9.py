def lone_teen(a, b):
    """
    We'll say that a number is "teen" if it is in the range 13..19 inclusive. Given 2 int values, return true if one or the other is teen, but not both.


    lone_teen(13, 99) → true
    lone_teen(21, 19) → true
    lone_teen(13, 13) → false
    """

    return (13 <= a <= 19) != (13 <= b <= 19)

print(lone_teen(13, 99))
print(lone_teen(21, 19))
print(lone_teen(13, 13))