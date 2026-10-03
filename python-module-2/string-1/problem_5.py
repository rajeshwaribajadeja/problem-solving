def endsly(str):
    """
    Given a string, return true if it ends in "ly".


    endsly("oddly") → true
    endsly("y") → false
    endsly("oddy") → false
    """
    return str[-2:] == "ly"
    # return str.endswith("ly")

print(endsly("oddly"))
print(endsly("y"))
print(endsly("oddy"))