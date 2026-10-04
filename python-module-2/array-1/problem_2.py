def make_last(nums):
    """
    Given an int array, return a new array with double the length where
    its last element is the same as the original array, and all the
    other elements are 0.

    make_last([4, 5, 6]) → [0, 0, 0, 0, 0, 6]
    make_last([1, 2]) → [0, 0, 0, 2]
    make_last([3]) → [0, 3]
    """

    result = [0] * (len(nums) * 2-1) + nums[-1:]

    return result


print(make_last([4, 5, 6]))
print(make_last([1, 2]))
print(make_last([3]))
