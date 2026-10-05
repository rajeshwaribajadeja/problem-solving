def right_digit(nums):
    """
    Given a list of non-negative integers, return an integer list
    of the rightmost digits. (Note: use %)


    right_digit([1, 22, 93]) → [1, 2, 3]
    right_digit([16, 8, 886, 8, 1]) → [6, 8, 6, 8, 1]
    right_digit([10, 0]) → [0, 0]
    """

    return list(map(lambda x: x % 10, nums))


print(right_digit([1, 22, 93]))
print(right_digit([16, 8, 886, 8, 1]))
print(right_digit([10, 0]))
