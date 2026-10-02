def xyz_there(str):
    """
    Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.


    xyz_there('abcxyz') → True
    xyz_there('abc.xyz') → False
    xyz_there('xyz.abc') → True
    """

    for i in range(len(str) - 2):
        if str[i:i+3] == "xyz":
            if i == 0 or str[i-1] != ".":
                return True

    return False

print(xyz_there('abcxyzabc'))
print(xyz_there('abc.xyzabc'))
print(xyz_there('xyzabc.xyz'))

