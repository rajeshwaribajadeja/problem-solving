def evenly_spaced(a, b, c):
    """
    Given three ints, a b c, one of them is small, one is medium and one is large. Return true if the three values are evenly spaced, so the difference between small and medium is the same as the difference between medium and large.


    evenly_spaced(2, 4, 6) → True
    evenly_spaced(4, 6, 2) → True
    evenly_spaced(4, 6, 3) → False
    """

    small = min(a, b, c)
    large = max(a, b, c)
    medium = a + b + c - small - large

    return medium - small == large - medium


print(evenly_spaced(2, 4, 6))
print(evenly_spaced(4, 6, 2))
print(evenly_spaced(4, 6, 3))