def copy_endy(nums, count):
    """
    We'll say that a positive int n is "endy" if it is in the range 0..10 or 90..100 (inclusive). Given an array of positive ints, return a new array of length "count" containing the first endy numbers from the original array. Decompose out a separate isEndy(int n) method to test if a number is endy. The original array will contain at least "count" endy numbers.


    copy_endy([9, 11, 90, 22, 6], 2) → [9, 90]
    copy_endy([9, 11, 90, 22, 6], 3) → [9, 90, 6]
    copy_endy([12, 1, 1, 13, 0, 20], 2) → [1, 1]
    """

    result = []

    for num in nums:
        if is_endy(num):
            result.append(num)

            if len(result) == count:
                break

    return result


def is_endy(n):
    return 0 <= n <= 10 or 90 <= n <= 100


print(copy_endy([9, 11, 90, 22, 6], 2))
print(copy_endy([9, 11, 90, 22, 6], 3))
print(copy_endy([12, 1, 1, 13, 0, 20], 2))