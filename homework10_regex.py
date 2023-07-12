"""
Homework10.

Description:
    open input.txt file and
    find all small english letters that match such conditions:
    target small letter round exactly with three capital english letters
    on the left and on the right

    Match examples:
    sdTRYaUVKn  -> matches "a"
    NTRSjARTb   -> no match ( not exactly 3 capital letters on the left)
    zDFGbOPNq   -> matches "b"
    Print Output as : "Result: "<your_found_human_readable_string">
"""

import re

input_file = 'input_homework10.txt'

# open input file in read mode

with open(input_file) as fh:
    text = fh.read()

#  find matched letters according to task conditions

# (?<=pre condition ) and (?=post condition)
pattern = r"""(?<=[^A-Z][A-Z]{3})  # pre-conditions
                [a-z]  # find any small english letter
                (?=[A-Z]{3}[^A-Z])  # post-conditions"""
reg_object = re.compile(pattern, re.M | re.X)
find_letters = reg_object.findall(text)
result = ''.join([str(letter) for letter in find_letters])
print(f'Result: {result}')
