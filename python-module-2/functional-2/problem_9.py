def square_56(nums):
    """
    Given a list of integers, return a list of those numbers squared
    and 10 added, omitting any of the resulting numbers that end in
    5 or 6.


    square_56([3, 1, 4]) → [19, 11]
    square_56([1]) → [11]
    square_56([2]) → [14]
    """

    nums = list(map(lambda x: x * x + 10, nums))

    return list(filter(lambda x: x % 10 != 5 and x % 10 != 6, nums))


print(square_56([3, 1, 4]))
print(square_56([1]))
print(square_56([2]))
