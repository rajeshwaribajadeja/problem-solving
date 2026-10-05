def fizz_array_2(n):
    """
    Given a number n, create and return a new string array of length n, containing the strings "0", "1" "2" .. through n-1. N may be 0, in which case just return a length 0 array.Given a number n, create and return a new string array of length n, containing the strings "0", "1" "2" .. through n-1. N may be 0, in which case just return a length 0 array.

    fizz_array_2(4) → ["0", "1", "2", "3"]
    fizz_array_2(10) → ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    fizz_array_2(2) → ["0", "1"]
    """

    nums = []

    for i in range(n):
        nums.append(str(i))

    return nums


print(fizz_array_2(4))
print(fizz_array_2(10))
print(fizz_array_2(2))
