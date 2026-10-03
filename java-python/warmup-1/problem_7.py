def in1020(a, b):
    """
    Given 2 int values, return true if either of them is in the range 10..20 inclusive.


    in1020(12, 99) → true
    in1020(21, 12) → true
    in1020(8, 99) → false
    """

    return 10 <= a <= 20 or 10 <= b <= 20

print(in1020(12, 99))
print(in1020(21, 12))
print(in1020(8, 99))