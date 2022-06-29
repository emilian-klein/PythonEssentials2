"""
Task:
    Your task is to write a program which is able to simulate the work of a seven-segment display.
    Each digit is constructed from 13 LEDs.
    Your code has to display any non-negative integer number entered by the user.
"""


digits_depiction = {
    '0': ("###", "# #", "# #", "# #", "###"),
    '1': ("  #", "  #", "  #", "  #", "  #"),
    '2': ("###", "  #", "###", "#  ", "###"),
    '3': ("###", "  #", "###", "  #", "###"),
    '4': ("# #", "# #", "###", "  #", "  #"),
    '5': ("###", "#  ", "###", "  #", "###"),
    '6': ("###", "#  ", "###", "# #", "###"),
    '7': ("###", "  #", "  #", "  #", "  #"),
    '8': ("###", "# #", "###", "# #", "###"),
    '9': ("###", "# #", "###", "  #", "###")
}


def get_number_to_display():
    """
    Gets number from user.
    Accepts only a non-negative integer.

    Returns
    ----------
    number : int
        Number to display as output.
    """
    number = None
    while True:
        try:
            number = int(input("What number should be displayed: "))
            if number < 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("That's not a non-negative integer.")
            continue
        except KeyboardInterrupt:
            print("Program ended.")
            exit()
    return number


def display_number(number):
    """
    Creates list which is holding representation of digits provided by user.
    Prints chosen digits segments line by line.

    Returns
    ----------
    None
    """
    digits = [digits_depiction[digit] for digit in str(number)]
    for i in range(5):
        print("  ".join(segment[i] for segment in digits))


while True:
    n = get_number_to_display()
    display_number(n)
