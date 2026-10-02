def reverse3(nums):
    """
    Given an array of ints length 3, return an array with the elements in reverse order and return [3, 2, 1].

    reverse3([1, 2, 3]) → [3, 2, 1]
    reverse3([5, 11, 9]) → [9, 11, 5]
    reverse3([7, 0, 0]) → [0, 0, 7]
    """

    # return [nums[2], nums[1], nums[0]]
    
    return nums[::-1]
    

print(reverse3([1, 2, 3]))
print(reverse3([5, 11, 9]))
print(reverse3([7, 0, 0]))
