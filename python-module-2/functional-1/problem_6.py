def math_1(nums):
    """
    Given a list of integers, return a list where each integer
    is added to 1 and the result is multiplied by 10.


    math_1([1, 2, 3]) → [20, 30, 40]
    math_1([6, 8, 6, 8, 1]) → [70, 90, 70, 90, 20]
    math_1([10]) → [110]
    """

    return list(map(lambda x: (x + 1) * 10, nums))


print(math_1([1, 2, 3]))
print(math_1([6, 8, 6, 8, 1]))
print(math_1([10]))
