def string_e(str):
    """
    Return true if the given string contains between 1 and 3 'e' chars.


    string_e("Hello") → true
    string_e("Heelle") → true
    string_e("Heelele") → false
    """
    count = 0
    for i in str:
        if i == "e":
            count += 1

    return 1 <= count <= 3

    # return 1 <= str.count("e") <= 3

print(string_e("Hello"))
print(string_e("Heelle"))
print(string_e("Heelele"))