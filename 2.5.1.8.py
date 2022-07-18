"""
Task:
    Your task is to write a program which:
    - asks the user for two separate texts;
    - checks whether, the entered texts are anagrams and prints the result.
Note:
    - assume that two empty strings are not anagrams;
    - treat upper- and lower-case letters as equal;
    - spaces are not taken into account during the check - treat them as non-existent
"""


def get_text(message):
    """
    Asks user to input a text.

    Returns
    ----------
    text : str
        text which is going to be checked if it is an anagram

    Parameters
    ----------
    message : str
        message to be displayed to user
    """
    text = input(message)
    return text


def delete_whitespaces(text):
    """
    Deletes all whitespaces from provided text.

    Returns
    ----------
    text_no_whitespaces : str
        text without whitespaces
    """
    text_no_whitespaces = "".join(text.split())
    return text_no_whitespaces


def count_characters(text):
    """
    Counts occurrences of all characters in given text.

    Returns
    ----------
    counted_characters : dict
        counted characters stored in dictionary form, where key is a specific character and value is its number of occurrences
    """
    counted_characters = {}
    for char in text:
        char_occurrences = text.count(char)
        if char not in counted_characters.keys():
            counted_characters[char] = char_occurrences
    return counted_characters


def is_anagram(text1, text2):
    """
    Checks if two provided strings are anagrams, outputs proper message.

    Returns
    ----------
    None
    """
    text1 = delete_whitespaces(text1)
    text2 = delete_whitespaces(text2)
    if len(text1) == 0 and len(text2) == 0:
        print("It is NOT an anagram.")
    else:
        text1_chars = count_characters(text1.lower())
        text2_chars = count_characters(text2.lower())
        if text1_chars == text2_chars:
            print("It is an anagram.")
        else:
            print("It is NOT an anagram.")


def main():
    """
    Main program loop.

    Returns
    ----------
    None
    """
    try:
        while True:
            text1 = get_text("Pass first sentence: ")
            text2 = get_text("Pass second sentence: ")
            is_anagram(text1, text2)
    except KeyboardInterrupt:
        exit()


main()
