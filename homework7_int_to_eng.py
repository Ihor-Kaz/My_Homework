"""
Homework7.

Description:
    Convert a non-negative integer num to its English words representation.
    Example 1:
    Input: num = 123
    Output: "One Hundred Twenty Three"

    let's take that number always > 100 and only three digits
    100 <= num <= 999
"""

digits = ['', 'One', 'Two', 'Three', 'Four',
          'Five', 'Six', 'Seven', 'Eight', 'Nine']
tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty',
        'Sixty', 'Seventy', 'Eighty', 'Ninety']
teen_numbers = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
                'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

numbers = int(input('Please, enter 3 digits between 100 and 999: '))

# Convert hundreds to word
input_hundreds = numbers // 100
words = f'{digits[input_hundreds]} Hundred'

# Convert tens and one digit to words
input_tens = (numbers % 100) // 10
input_digit = (numbers % 10)
if input_tens == 0:
    words += f' {digits[input_digit]}'
elif input_tens == 1:
    words += f' and {teen_numbers[input_digit]}'
else:
    words += f' {tens[input_tens]} {digits[input_digit]}'

print(words)
