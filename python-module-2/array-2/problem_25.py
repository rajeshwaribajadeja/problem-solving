def without_ten(nums):
    """
    Return a version of the given array where all the 10's have been removed. The remaining elements should shift left towards the start of the array as needed, and the empty spaces a the end of the array should be 0. So {1, 10, 10, 2} yields {1, 2, 0, 0}. You may modify and return the given array or make a new array.


    without_ten([1, 10, 10, 2]) → [1, 2, 0, 0]
    without_ten([10, 2, 10]) → [2, 0, 0]
    without_ten([1, 99, 10]) → [1, 99, 0]
    """

    result = []

    for num in nums:
        if num != 10:
            result.append(num)

    while len(result) < len(nums):
        result.append(0)

    return result


print(without_ten([1, 10, 10, 2]))
print(without_ten([10, 2, 10]))
print(without_ten([1, 99, 10]))
