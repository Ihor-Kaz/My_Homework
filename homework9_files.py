"""
Homework9.

Description:
    write script that will read "input.txt" file and find there
    all characters from english alphabet
    collect these characters and their positions in file
    after info collected
    this info as text write to "output.txt" file in such format
    ####################
    <first found letter> -> pos1
    <next_letter> -> pos2
    <next_letter -> pos3
    etc
    #######################
"""

import re

fh = None
letters = []
input_file = 'input.txt'
output_file = 'output.txt'

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

# find characters and their positions inside the 'input' file

for letter in re.finditer(r'[a-zA-Z]', l1):
    letters.append(f'{letter.group()} -> {letter.span()}')
result = '\n'.join(letters)
print(result)

# create output file in write mode and write result into it

try:
    fh = open(output_file, 'w')
    fh.write(result)
    print(f'writing to {output_file} is completed successfully')
except Exception as g_exc:
    print(g_exc)
finally:
    print(f'file {output_file} is closed')
    if fh:
        fh.close()
