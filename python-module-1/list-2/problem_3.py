from importlib import machinery
def centered_average(nums):
    """
    Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

    centered_average([1, 2, 3, 4, 100]) → 3
    centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
    centered_average([-10, -4, -2, -4, -2, 0]) → -3
    """

    sum = 0
    count = len(nums) - 2
    min_val = min(nums)
    max_val = max(nums)

    for n in nums:
        sum += n

    count = len(nums) - 2
    total = sum - min(nums) - max(nums)
    
    return int(total / count)

print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))