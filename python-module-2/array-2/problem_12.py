def has_12(nums):
    """
    Given an array of ints, return true if there is a 1 in the array
    with a 2 somewhere later in the array.

    has_12([1, 3, 2]) → True
    has_12([3, 1, 2]) → True
    has_12([3, 1, 4, 5, 2]) → True
    """

    found_1 = False

    for num in nums:
        if num == 1:
            found_1 = True

        if num == 2 and found_1:
            return True

    return False


print(has_12([1, 3, 2]))
print(has_12([3, 1, 2]))
print(has_12([3, 1, 4, 5, 2]))
