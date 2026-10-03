def in3050(a, b):
    """
    Given 2 int values, return true if they are both in the range 30..40 inclusive, or they are both in the range 40..50 inclusive.


    in3050(30, 31) → true
    in3050(30, 41) → false
    in3050(40, 50) → true
    """

    return (30 <= a <= 40 and 30 <= b <= 40) or (40 <= a <= 50 and 40 <= b <= 50)

print(in3050(30, 31))
print(in3050(30, 41))
print(in3050(40, 50))
        