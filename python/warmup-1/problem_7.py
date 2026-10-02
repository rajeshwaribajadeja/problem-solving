def near_hundred(n):
    """
    Given an int n, return True if it is within 10 of 100 (in the range 90..110) or within 10 of 200 (in the range 190..210).


    near_hundred(93) → True
    near_hundred(90) → True
    near_hundred(89) → False
    """
    return (abs(n - 100) <= 10) or (abs(n - 200) <= 10)


print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))