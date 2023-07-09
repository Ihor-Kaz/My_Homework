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

fh = None

input_file = 'input_homework10.txt'

# open input file in read more

try:
    fh = open(input_file)
    l1 = fh.read()
    print(f'reading from {input_file} is completed successfully')
except Exception as g_exc:
    print(g_exc)
finally:
    print(f'file {input_file} is closed')
    if fh:
        fh.close()

#    find all small english letters that match such conditions:
#    target small letter round exactly with three capital english letters
#    on the left and on the right

# verbose

result = re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', l1, re.MULTILINE)
result = ''.join([str(letter) for letter in result])
print(f'Result: {result}')

result = re.compile(r"""[^A-Z]  # find all letters except A-Z
                        [A-Z]{3}  # find next three A-Z letters in a row
                        after any symbol
                        [a-z]  # find any small english letter
                        after previous step
                        [A-Z]{3}  # find next three A-Z letters in a row
                        after small letter
                        [^A-Z]  # find all letters except A-Z""", re.VERBOSE)
