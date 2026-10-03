def extra_end(str):
    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string.

    extra_end('Hello') → 'lolo'
    extra_end('ab') → 'abab'
    extra_end('Hi') → 'HiHiHi'  
    """

    return str[-2:] * 3

print(extra_end('Hello'))
print(extra_end('ab'))
print(extra_end('Hi'))
