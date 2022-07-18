"""
Digit of Life is a digit evaluated using somebody's birthday.
It's simple - you just need to sum all the digits of the date.
If the result contains more than one digit, you have to repeat the addition until you get exactly one digit.

For example:
1 January 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3

Task:
    Your task is to write a program which:
    - asks the user her/his birthday (in the format YYYYMMDD or YYYYDDMM or MMDDYYYY)
    - outputs the "Digit of Life" for the date.
"""


def get_birthday():
    """
    Asks user for birthday date.

    Returns
    ----------
    birthday_date : str
        string containing birthday date
    """
    birthday_date = input("When is your birthday? (Pass date in YYYYMMDD format) ")
    return birthday_date


def calculate_digit_of_life(birthday_date):
    """
    Calculates digit of life based on provided instructions.

    Returns
    ----------
    result : str
        digit of life
    """
    digits = [int(digit) for digit in birthday_date.strip()]
    while True:
        result = str(sum(digits))
        if len(result) > 1:
            digits = [int(digit) for digit in result]
        else:
            break
    return result


def main():
    """
    Main program loop.

    Returns
    ----------
    None
    """
    try:
        while True:
            birthday_date = get_birthday()
            digit_of_life = calculate_digit_of_life(birthday_date)
            print("Your Digit of Life: ", digit_of_life)
    except KeyboardInterrupt:
        exit()


main()
