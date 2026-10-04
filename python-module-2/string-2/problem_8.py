def xyz_middle(str):
    """
    Given a string, does "xyz" appear in the middle of the string? To define middle, we'll say that the number of chars to the left and right of the "xyz" must differ by at most one. This problem is harder than it looks.


    xyz_middle("AAxyzBB") → true
    xyz_middle("AxyzBB") → true
    xyz_middle("AxyzBBB") → false
    """
    for i in range(len(str) - 2):
        if str[i:i+3] == 'xyz':
            left_length = len(str[:i])
            right_length = len(str[i + 3:])
            if abs(left_length - right_length) <= 1:
                return True
    return False

print(xyz_middle("AAxyzBB"))  
print(xyz_middle("AxyzBB"))   
print(xyz_middle("AxyzBBB"))      