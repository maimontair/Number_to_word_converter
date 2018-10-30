from decimal import *


def get_input_from_user():
    """
    This function prompts the user for a number.

    :return: string
    """
    try:
        num = raw_input("Please enter a number to convert: ")
    except (ValueError, SyntaxError):
        print ("Please enter a valid input")
        exit()
    return str(num).strip()


def strip_leading_zeros(number):
    """
    This function takes a string and removes all leading zeros in it. If the input is all 0s it will return "0".
    Else it will return the string without the leading 0s.

    :param number: string
    :return: string
    """
    num = number.lstrip("0")
    # if num is empty, it mean number was all zeros, so return "0"
    if not num or num == ".0":
        return "0"
    # else just remove leading zeros
    else:
        return number.lstrip("0")


def check_input(user_input):
    """
    This function checks that the user's input is correct and outputs an error message if it's not. The value has
    to be a number, between 0 and 99,999 and must not have more than one digit after the decimal point.

    :param user_input: string
    :return: bool
    """
    if not user_input.replace('.','',1).isdigit():
        print("Input must be a number. Please try again")
        return False
    input_num = Decimal(user_input)
    # checks that the input is in the right range -> 0 <= input < 1000,000
    if input_num < 0 or input_num > 99999:
        print("Input not in the right range. Value needs to be between 0 and 99,999. Please try again")
        return False
    # checks if decimal are up to one digit. Will allow multiple following 0s as long as there are no other digits.
    if input_num.as_tuple().exponent < -1:
        print ("Can only have one digit for decimal, please try again")
        return False
    return True


def convert_integer_part(num):
    """
    This function converts the integer part of the number to words.

    :param num: string
    :return: string
    """
    place = len(num) - 1
    index = 0
    output = ""
    if place == 0 and num[index] == '0':
        return "zero"
    while place >= 0 and index < len(num):
        # if at positions ones, thousand, etc.
        if place % 3 == 0 and num[index] != '0':
            output += base_dict[num[index]] + " "
        # if at positions tens, ten thousand, etc.
        elif place % 3 == 1 and num[index] != '0':
            if num[index] == '1':
                output += teens_dict[num[index + 1]] + " "
                index += 1
                place -= 1
            else:
                output += tens_dict[num[index]] + " "
        # if at the hundreds position
        elif place % 3 == 2 and num[index] != '0':
            output += base_dict[num[index]] + " hundred "
        # if at the thousands position, add 'thousand' to the string
        if place == 3:
            output += "thousand "

        place -= 1
        index += 1

    return output.strip()


def convert_decimal_part(num):
    """
    This function converts the decimal part of the number to words. If num is 0 it returns an empty string.

    :param num: string
    :return: string
    """
    if num != "0":
        decimal_output = " point " + base_dict[str(num[0])]
    else:
        decimal_output = ""
    return decimal_output


def split_number(number):
    """
    This function takes a string and split it at the decimal point into two strings.
    If there is no decimal point, it returns "0" for the second string.

    :param number:
    :return: string, string
    """
    parts = number.split(".", 1)
    # if there is a decimal point and a digit after it, return int and decimal parts separately
    if len(parts) == 2 and len(parts[1]) != 0:
        return parts[0], parts[1]
    # if there is no decimal point or if there is nothing after the decimal point,
    # return int part and return "0" to flag that there is no decimal digit
    else:
        return parts[0], "0"


base_dict = {'0': "", '1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six",
             '7': "seven", '8': "eight", '9': "nine"}

tens_dict = {'0': "", '1': "ten", '2': "twenty", '3': "thirty", '4': "forty", '5': "fifty", '6': "sixty",
             '7': "seventy", '8': "eighty", '9': "ninety"}

teens_dict = {'0': "ten", '1': "eleven", '2': "twelve", '3': "thirteen", '4': "fourteen", '5': "fifteen", '6': "sixteen",
              '7': "seventeen", '8': "eighteen", '9': "nineteen"}


def main():
    # get input from user
    number = get_input_from_user()
    # check that the input is valid
    if not check_input(number):
        exit()
    # strip leading zeros from input
    my_string = strip_leading_zeros(number)
    # separate the value to int and decimal parts
    int_part, decimal_part = split_number(my_string)
    # convert int part to words
    output = convert_integer_part(int_part)
    # convert decimal part to words
    output += convert_decimal_part(decimal_part)
    # print converted value
    print output.rstrip()


if __name__ == '__main__':
    main()
