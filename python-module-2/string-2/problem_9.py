"""String-2: get_sandwich problem solution."""


def get_sandwich(s: str) -> str:
    """Return the string between the first and last appearance of 'bread'.

    A sandwich is two pieces of bread with something in between. Return
    the string that is between the first and last appearance of "bread"
    in the given string, or return the empty string "" if there are not
    two pieces of bread.

    Args:
        s: The input string.

    Returns:
        The content between first and last "bread", or "" if < 2 "bread"s.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the extracted substring.

    Examples:
        >>> get_sandwich("breadjambread")
        'jam'
        >>> get_sandwich("xxbreadjambreadyy")
        'jam'
        >>> get_sandwich("xxbreadyy")
        ''
    """
    return (
        s[s.find("bread") + 5:s.rfind("bread")]
        if s.count("bread") >= 2
        else ""
    )

if __name__ == "__main__":
    print(get_sandwich("breadjambread"))
    print(get_sandwich("xxbreadjambreadyy"))
    print(get_sandwich("xxbreadyy"))