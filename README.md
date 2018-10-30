# Number to Word Converter 
The following program takes a number as input and returns that number written in words.

## Requirements
Python 2.7

pytest

## To Run
python number_converter.py

## To Run the Tests
Make sure to pip install pytest

From the root of the project run 'pytest'

### Assumptions made:
1) Leading zeros can be ignored
2) A decimal point without a following digit can be ignored
3) 00.0 can be returned as zero
4) Program can output error message and exit when the wrong value is entered
5) Trailing zeros won't be ignored - 9.50 would output an error and exit because 
it's more than one digit following the decimal point

