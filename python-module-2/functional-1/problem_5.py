def more_y(words):
    """
    Given a list of strings, return a list where each string
    has "y" added at its start and end.


    more_y(["a", "b", "c"]) → ["yay", "yby", "ycy"]
    more_y(["hello", "there"]) → ["yhelloy", "ytherey"]
    more_y(["yay"]) → ["yyayy"]
    """

    return list(map(lambda x: "y" + x + "y", words))


print(more_y(["a", "b", "c"]))
print(more_y(["hello", "there"]))
print(more_y(["yay"]))
