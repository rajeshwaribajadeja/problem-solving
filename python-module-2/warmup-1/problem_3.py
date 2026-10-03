def front22(str):
    """
    Given a string, take the first 2 chars and return the string with the 2 chars added at both the front and back, so "kitten" yields"kikittenki". If the string length is less than 2, use whatever chars are there.


    front22("kitten") → "kikittenki"
    front22("Ha") → "HaHaHa" 
    front22("abc") → "ababcab"
    """
    front = str[:2]
    return front + str + front

print(front22("kitten"))
print(front22("Ha"))
print(front22("abc"))