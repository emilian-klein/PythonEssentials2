"""
Task:
    The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on.
    Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.
    Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and
    all non-alphabetical characters should remain untouched.

    Your task is to write a program which:
    - asks the user for one line of text to encrypt,
    - asks the user for a shift value (an integer number from the range 1..25),
    - prints out the encoded text.
"""


def ask_for_sentence_to_encrypt():
    """
    Asks user what data should be encrypted with modified Caesar cipher.

    Returns
    ----------
    sentence_to_encrypt : str
        Sentence which is going to be encrypted.
    """
    sentence_to_encrypt = input("Sentence to encrypt: ")
    return sentence_to_encrypt


def ask_for_shift_value():
    """
    Gets from user number which is shift value.
    Accepts only integer from range 1 - 25.

    Returns
    ----------
    shift_value : int
        Shift value to be used in modified Caesar cipher.
    """
    shift_value = None
    while True:
        try:
            shift_value = int(input("Shift value: "))
            if shift_value < 1 or shift_value > 25:
                raise ValueError
            else:
                break
        except ValueError:
            print("That's not a valid integer.")
            continue
    return shift_value


def encrypt_message(sentence_to_encrypt, shift_value):
    """
    Encrypts sentence with modified Caesar cipher.
    Modulo operation is needed to change character to its correct substitute from ASCII table.

    Returns
    ----------
    encrypted_sentence : str
        Sentence which is encrypted with modified Caesar cipher.
    """
    encrypted_sentence = ""
    for char in sentence_to_encrypt:
        if char.isalpha():
            if char.isupper():
                encrypted_sentence += chr((ord(char) - 65 + shift_value) % 26 + 65)
            else:
                encrypted_sentence += chr((ord(char) - 97 + shift_value) % 26 + 97)
        else:
            encrypted_sentence += char
    return encrypted_sentence


def main():
    """
    Main program loop.

    Returns
    ----------
    None
    """
    try:
        while True:
            sentence_to_encrypt = ask_for_sentence_to_encrypt()
            shift_value = ask_for_shift_value()
            encrypted_sentence = encrypt_message(sentence_to_encrypt, shift_value)
            print("Encrypted sentence:", encrypted_sentence)
    except KeyboardInterrupt:
        exit()


main()
