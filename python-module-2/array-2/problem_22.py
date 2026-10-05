def post_4(nums):
    """
    Given a non-empty array of ints, return a new array containing the elements from the original array that come after the last 4 in the original array. The original array will contain at least one 4. Note that it is valid in java to create an array of length 0.

    post_4([2, 4, 1, 2]) → [1, 2]
    post_4([4, 1, 4, 2]) → [2]
    post_4([4, 4, 1, 2, 3]) → [1, 2, 3]
    """

    last_4 = 0
    
    for i in range(len(nums)):
        if nums[i] == 4:
            last_4 = i

    return nums[last_4 + 1:]


print(post_4([2, 4, 1, 2]))
print(post_4([4, 1, 4, 2]))
print(post_4([4, 4, 1, 2, 3]))
