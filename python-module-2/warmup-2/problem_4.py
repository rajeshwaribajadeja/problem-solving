def altpairs(str):
    """

    Given a string, return a string made of the chars at indexes 0,1, 4,5, 8,9 ... so "kittens" yields "kien".


    altpairs("kitten") → "kien"
    altpairs("Chocolate") → "Chole"
    altpairs("CodingHorror") → "Congrr"
    """
    result = ""

    for i in range(0, len(str), 4):
        result += str[i:i+2]

    return result

print(altpairs("kitten"))
print(altpairs("Chocolate"))
print(altpairs("CodingHorror"))