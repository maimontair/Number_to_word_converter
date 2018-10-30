import number_converter as converter


def test_check_input():
    assert converter.check_input("-10") is False
    assert converter.check_input("100000") is False
    assert converter.check_input("aaa") is False
    assert converter.check_input("100.11") is False
    assert converter.check_input("10.10") is False
    assert converter.check_input("10.00") is False
    assert converter.check_input("100..1") is False
    assert converter.check_input(".5") is True
    assert converter.check_input("100.1") is True
    assert converter.check_input("99999") is True
    assert converter.check_input("0") is True


def test_leading_zeros():
    assert converter.strip_leading_zeros("0000202") == "202"
    assert converter.strip_leading_zeros("00000") == "0"
    assert converter.strip_leading_zeros("100") == "100"
    assert converter.strip_leading_zeros("003.3") == "3.3"


def test_split_number():
    assert converter.split_number("100.1") == ("100", "1")
    assert converter.split_number("100") == ("100", "0")
    assert converter.split_number("0.1") == ("0", "1")
    assert converter.split_number("54100.9") == ("54100", "9")


def test_int_convert_valid_values():
    assert converter.convert_integer_part("100") == "one hundred"
    assert converter.convert_integer_part("50") == "fifty"
    assert converter.convert_integer_part("11111") == "eleven thousand one hundred eleven"
    assert converter.convert_integer_part("0") == "zero"
    assert converter.convert_integer_part("50569") == "fifty thousand five hundred sixty nine"
    assert converter.convert_integer_part("111") == "one hundred eleven"
    assert converter.convert_integer_part("4032") == "four thousand thirty two"
    assert converter.convert_integer_part("87413") == "eighty seven thousand four hundred thirteen"
    assert converter.convert_integer_part("45") == "forty five"


def test_decimal_convert():
    assert converter.convert_decimal_part("1") == " point one"
    assert converter.convert_decimal_part("5") == " point five"
    assert converter.convert_decimal_part("0") == ""











