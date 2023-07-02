"""
Homework8.

Description:
    Given the list of integers ( positive , negative, zeros)
    Find max multiplication of three values in list
    l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]

    Input: [-1, 1, 2, 0, 3, 12, 4, 5, -1, 6]
    Output: Max value = "360". Nums are: (12, 5, 6)

    Input: [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]
    Output: Max value = "2016". Nums are: (-7, 12, -24)

"""

l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]

# create a list with negative nums replaced to positive one
converted = []
for num in l1:
    if num < 0:
        num = num * -1
        converted.append(num)

# merge the original list and the converted one
merged = l1 + converted

# sort list
sorted_list = sorted(merged, reverse=True)

# take 3 max int and multiplication them
result = sorted_list[0] * sorted_list[1] * sorted_list[2]

print(f'Max value = "{result}". Nums are: {sorted_list[:3]}')
