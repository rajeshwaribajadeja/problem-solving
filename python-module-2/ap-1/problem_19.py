def user_compare(name_a, id_a, name_b, id_b):
    """
    We have data for two users, A and B, each with a String name and an int id. The goal is to order the users such as for sorting. Return -1 if A comes before B, 1 if A comes after B, and 0 if they are the same. Order first by the string names, and then by the id numbers if the names are the same. Note: with Strings str1.compareTo(str2) returns an int value which is negative/0/positive to indicate how str1 is ordered to str2 (the value is not limited to -1/0/1). (On the AP, there would be two User objects, but here the code simply takes the two strings and two ints directly. The code logic is the same.)


    user_compare("bb", 1, "zz", 2) → -1
    user_compare("bb", 1, "aa", 2) → 1
    user_compare("bb", 1, "bb", 1) → 0
    """

    if name_a < name_b:
        return -1

    if name_a > name_b:
        return 1

    if id_a < id_b:
        return -1

    if id_a > id_b:
        return 1

    return 0


print(user_compare("bb", 1, "zz", 2))
print(user_compare("bb", 1, "aa", 2))
print(user_compare("bb", 1, "bb", 1))