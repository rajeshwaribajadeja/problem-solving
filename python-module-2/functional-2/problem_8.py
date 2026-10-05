def two_2(nums):
    """
    Given a list of non-negative integers, return a list of those numbers
    multiplied by 2, omitting any of the resulting numbers that end in 2.


    two_2([1, 2, 3]) → [4, 6]
    two_2([2, 6, 11]) → [4]
    two_2([0]) → [0]
    """

    nums = list(map(lambda x: x * 2, nums))

    return list(filter(lambda x: x % 10 != 2, nums))


print(two_2([1, 2, 3]))
print(two_2([2, 6, 11]))
print(two_2([0]))
