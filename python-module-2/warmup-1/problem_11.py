def mix_start(str):
    """
    Return true if the given string begins with "mix", except the 'm' can be anything, so "pix", "9ix" .. all count.

    mix_start("mix snacks") → true
    mix_start("pix snacks") → true
    mix_start("piz snacks") → false
    """

    return len(str) >= 3 and str[1:3] == "ix"

print(mix_start("mix snacks"))
print(mix_start("pix snacks"))
print(mix_start("piz snacks"))