def fizz_array(n):
    """
    Given a number n, create and return a new int array of length n, containing the numbers 0, 1, 2, ... n-1. The given n may be 0, in which case just return a length 0 array. You do not need a separate if-statement for the length-0 case; the for-loop should naturally execute 0 times in that case, so it just works. The syntax to make a new int array is: new int[desired_length]

    fizz_array(4) → [0, 1, 2, 3]
    fizz_array(1) → [0]
    fizz_array(10) → [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """

    nums = []

    for i in range(n):
        nums.append(i)

    return nums


print(fizz_array(4))
print(fizz_array(1))
print(fizz_array(10))
