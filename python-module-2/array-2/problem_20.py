def ten_run(nums):
    """
    For each multiple of 10 in the given array, change all the values following it to be that multiple of 10, until encountering another multiple of 10. So {2, 10, 3, 4, 20, 5} yields {2, 10, 10, 10, 20, 20}.

    ten_run([2, 10, 3, 4, 20, 5]) → [2, 10, 10, 10, 20, 20]
    ten_run([10, 1, 20, 2]) → [10, 10, 20, 20]
    ten_run([10, 1, 9, 20]) → [10, 10, 10, 20]
    """

    result = []
    current = None

    for num in nums:
        if num % 10 == 0:
            current = num

        if current is not None:
            result.append(current)
        else:
            result.append(num)

    return result


print(ten_run([2, 10, 3, 4, 20, 5]))
print(ten_run([10, 1, 20, 2]))
print(ten_run([10, 1, 9, 20]))
