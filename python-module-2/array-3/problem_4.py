def can_balance(nums):
    """
    Given a non-empty array, return true if there is a place to split
    the array so that the sum of the numbers on one side is equal to
    the sum of the numbers on the other side.

    can_balance([1, 1, 1, 2, 1]) → True
    can_balance([2, 1, 1, 2, 1]) → False
    can_balance([10, 10]) → True
    """

    total = sum(nums)
    left_sum = 0

    for num in nums:
        left_sum += num

        if left_sum == total - left_sum:
            return True

    return False


print(can_balance([1, 1, 1, 2, 1]))
print(can_balance([2, 1, 1, 2, 1]))
print(can_balance([10, 10]))
