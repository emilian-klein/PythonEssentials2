"""
Task:
    Your task is to write a program which:
    - asks the user for some text;
    - checks whether the entered text is a palindrome, and prints result.
Note:
    - assume that an empty string isn't a palindrome;
    - treat upper-case and lower-case letters as equal;
    - spaces are not taken into account during the check - treat them as non-existent;
"""


def ask_for_sentence_to_check():
    """
    Asks user what sentence should be checked to be palindrome.

    Returns
    ----------
    sentence_to_check : str
        Sentence which is going to be checked.
    """
    sentence_to_check = input("Sentence to check: ")
    return sentence_to_check


def is_palindrome(sentence):
    """
    Checks if sentence is a palindrome. Treats upper-case and lower-case letters equally.

    Returns
    ----------
    None
    """
    sentence = delete_whitespaces(sentence)
    sentence = sentence.casefold()
    if len(sentence) == 0:
        print("It is not a palindrome.")
    elif sentence == sentence[::-1]:
        print("It is a palindrome.")
    else:
        print("It is NOT a palindrome.")


def delete_whitespaces(sentence):
    """
    Deletes all whitespaces from sentence as they are not taken into account.

    Returns
    ----------
    sentence : str
        sentence without whitespaces
    """
    sentence = "".join(sentence.split())
    return sentence


def main():
    """
    Main program loop.

    Returns
    ----------
    None
    """
    try:
        while True:
            sentence = ask_for_sentence_to_check()
            is_palindrome(sentence)
    except KeyboardInterrupt:
        exit()


main()
