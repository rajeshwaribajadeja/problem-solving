def have_three(nums):
    """
    Given an array of ints, return true if the value 3 appears in the array
    exactly 3 times, and no 3's are next to each other.

    have_three([3, 1, 3, 1, 3]) → True
    have_three([3, 1, 3, 3]) → False
    have_three([3, 4, 3, 3, 4]) → False
    """
    # solution-1

    # count = 0

    # for i in range(len(nums)):
    #     if nums[i] == 3:
    #         count += 1

    #         if i > 0 and nums[i - 1] == 3:
    #             return False

    # return count == 3

    # solution-2
    # if nums.count(3) != 3:
    #     return False

    # for i in range(len(nums) - 1):
    #     if nums[i] == 3 and nums[i + 1] == 3:
    #         return False

    # return True

    # solution-3
    # pos = [i for i, num in enumerate(nums) if num == 3]
    pos = [i for i in range(len(nums)) if nums[i] == 3]

    return (
        len(pos) == 3
        and pos[1] - pos[0] > 1
        and pos[2] - pos[1] > 1
    )


print(have_three([3, 1, 3, 1, 3]))
print(have_three([3, 1, 3, 3]))
print(have_three([3, 4, 3, 3, 4]))
