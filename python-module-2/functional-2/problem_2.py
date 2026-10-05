def no_9(nums):
    """
    Given a list of non-negative integers, return a list of those numbers
    except omitting any that end with 9. (Note: % by 10)


    no_9([1, 2, 19]) → [1, 2]
    no_9([9, 19, 29, 3]) → [3]
    no_9([1, 2, 3]) → [1, 2, 3]
    """

    return list(filter(lambda x: x % 10 != 9, nums))


print(no_9([1, 2, 19]))
print(no_9([9, 19, 29, 3]))
print(no_9([1, 2, 3]))
