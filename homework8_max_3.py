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

# create a list where each element is squared
converted = [num**2 for num in l1]

# sort list
sorted_list = sorted(converted, reverse=True)

# create new list with elements = squared element from original list
new_list = []
for el in sorted_list:
    for num in l1:
        if num**2 == el:
            new_list.append(num)

# take first 3 int and multiplication them
result = new_list[0] * new_list[1] * new_list[2]

print(f'Max value = "{result}". Nums are: {new_list[:3]}')
