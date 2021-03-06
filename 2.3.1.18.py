"""
Task:
    Write function, which behaves almost exactly like the original split() method:
    - it should accept exactly one argument - a string,
    - it should return a list of words created from the string, divided in the places where the string contains whitespaces,
    - if the string is empty, the function should return an empty list,
    - its name should be mysplit().
"""


def mysplit(string):
    """
    Splits given string on each occurrence of whitespaces.
    Returns empty list if given string is empty.

    Returns
    ----------
    output_list : list
        Splitted characters/words as list of strings.
    """
    output_list = []
    substring = ""
    for character in string:
        if character != " ":
            substring += character
        elif substring != "":
            output_list.append(substring)
            substring = ""
    if substring != "":
        output_list.append(substring)
    return output_list 


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
