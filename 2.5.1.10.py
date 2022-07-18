"""
Task:
    Given two strings: one being a word (e.g., "dog") and the second being a combination of any characters.
    Write a program which answers the following question: are the characters comprising the first string hidden inside the second string?
    Don't worry about case sensitivity.
"""


def get_text(message):
    """
    Asks user to input a text.

    Returns
    ----------
    text : str
        text from user

    Parameters
    ----------
    message : str
        message to be displayed to user
    """
    text = input(message)
    return text


def find_chars(word, char_combination):
    """
    Checks if every character in "word" is present is "char_combination".
    If is than deletes that character from char_combination list and moves on, otherwise loop is terminated.

    Returns
    ----------
    True or False : bool
        True if all characters were found, False otherwise
    """
    word = word.strip().lower()
    char_combination = char_combination.strip().lower()
    char_combination = list(char_combination)
    for char in word:
        if char in char_combination:
            char_index = char_combination.index(char)
            char_combination.pop(char_index)
        else:
            return False
    return True


def main():
    """
    Main program loop.

    Returns
    ----------
    None
    """
    try:
        while True:
            word = get_text("Pass word: ")
            char_combination = get_text("Pass character combination: ")
            if find_chars(word, char_combination):
                print(f"Word '{word}' can be constructed using characters in '{char_combination}'")
            else:
                print(f"Word '{word}' can NOT be constructed using characters in '{char_combination}'")
    except KeyboardInterrupt:
        exit()


main()
