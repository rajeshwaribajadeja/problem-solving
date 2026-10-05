def max_span(nums):
    """
    Consider the leftmost and righmost appearances of some value in an array. We'll say that the "span" is the number of elements between the two inclusive. A single value has a span of 1. Returns the largest span found in the given array. 
    
    max_span([1, 2, 1, 1, 3]) → 4
    max_span([1, 4, 2, 1, 4, 1, 4]) → 6
    max_span([1, 4, 2, 1, 4, 4, 4]) → 6
    """

    max_span = 0

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] == nums[j]:
                span = j - i + 1
                if span > max_span:
                    max_span = span

    return max_span


print(max_span([1, 2, 1, 1, 3]))
print(max_span([1, 4, 2, 1, 4, 1, 4]))
print(max_span([1, 4, 2, 1, 4, 4, 4]))