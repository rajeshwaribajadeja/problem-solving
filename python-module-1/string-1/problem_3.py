"""String-1: make_tags problem solution."""


def make_tags(tag: str, word: str) -> str:
    """Create an HTML string wrapping the word in opening and closing tags.

    The web is built with HTML strings like "<i>Yay</i>". Given tag and
    word strings, create the HTML string with tags around the word.

    Args:
        tag: The HTML tag name.
        word: The content string to wrap.

    Returns:
        The formatted HTML tag string.

    Complexity:
        Time Complexity: O(len(tag) + len(word)).
        Space Complexity: O(len(tag) + len(word)) to store the tagged string.

    Examples:
        >>> make_tags('i', 'Yay')
        '<i>Yay</i>'
        >>> make_tags('i', 'Hello')
        '<i>Hello</i>'
    """
    return f"<{tag}>{word}</{tag}>"


if __name__ == "__main__":
    print(make_tags("i", "Yay"))
    print(make_tags("i", "Hello"))