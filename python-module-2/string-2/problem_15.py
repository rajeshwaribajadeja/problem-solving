
def word_ends(str, word):
    """
    Given a string and a non-empty word string, return a string made of each char just before and just after every appearance of the word in the string. Ignore cases where there is no char before or after the word, and a char may be included twice if it is between two words.


    word_ends("abcXY123XYijk", "XY") → "c13i"
    word_ends("XY123XY", "XY") → "13"
    word_ends("XY1XY", "XY") → "11"
    """

    result = ""
    i = 0

    while i < len(str):
        if str[i:i+len(word)] == word:
            if i > 0:
                result += str[i-1]
            if i+len(word) < len(str):
                result += str[i+len(word)]
            i += len(word)
        else:
            i += 1
        

    return result

print(word_ends("abcXY123XYijk", "XY"))
print(word_ends("XY123XY", "XY"))
print(word_ends("XY1XY", "XY"))
