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

# create a dict where key = multiplication and value = (a, b, c)
d = {}
for a in range(len(l1)):
    for b in range(a + 1, len(l1)):
        for c in range(b + 1, len(l1)):
            multiplication = l1[a] * l1[b] * l1[c]
            d.update({multiplication: (l1[a], l1[b], l1[c])})

# take a max from created dict
maximum = max(d)
print(f'Max value = "{maximum}". Nums are: {d.get(maximum)}')
