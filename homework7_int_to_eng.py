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

digits = {0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
          5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}

tens = {1: 'Ten', 2: 'Twenty', 3: 'Thirty', 4: 'Forty',
        5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}

teen_numbers = {1: 'Eleven', 2: 'Twelve', 3: 'Thirteen',
                4: 'Fourteen', 5: 'Fifteen', 6: 'Sixteen', 7: 'Seventeen',
                8: 'Eighteen', 9: 'Nineteen'}

numbers = int(input('Please, enter 3 digits between 100 and 999: '))

# Split into hundreds, tens and digits
input_hundreds = numbers // 100
input_tens = (numbers % 100) // 10
input_digit = (numbers % 10)

# Convert hundreds, tens and one digit to words
words = f'{digits[input_hundreds]} Hundred'
if input_tens == 0:
    words += f' {digits[input_digit]}'
elif input_tens == 1:
    words += f' {teen_numbers[input_digit]}'
else:
    words += f' {tens[input_tens]} {digits[input_digit]}'

print(words)
