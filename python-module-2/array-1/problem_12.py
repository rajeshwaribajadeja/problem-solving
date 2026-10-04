def front_piece(nums):
    """
    Given an int array of any length, return a new array of its first
    2 elements. If the array is smaller than length 2, use whatever
    elements are present.

    front_piece([1, 2, 3]) → [1, 2]
    front_piece([1, 2]) → [1, 2]
    front_piece([1]) → [1]
    """

    return nums[:2]


print(front_piece([1, 2, 3]))
print(front_piece([1, 2]))
print(front_piece([1]))
