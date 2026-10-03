def no_triples(nums):
    """
    Given an array of ints, we'll say that a triple is a value appearing 3 times in a row in the array. Return true if the array does not contain any triples.

    no_triples([1, 1, 2, 2, 1]) → true
    no_triples([1, 1, 2, 2, 2, 1]) → false
    no_triples([1, 1, 1, 2, 2, 2, 1]) → false
    """

    for i in range(len(nums)-2):
        
        # if nums[i] == nums[i+1] and nums[i] == nums[i+2]:
        if nums[i] == nums[i+1] == nums[i+2]:
            return False

    return True

print(no_triples([1, 1, 2, 2, 1]))
print(no_triples([1, 1, 2, 2, 2, 1]))
print(no_triples([1, 1, 1, 2, 2, 2, 1]))