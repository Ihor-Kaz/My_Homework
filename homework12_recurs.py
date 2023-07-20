"""
Homework12.

Description:
    Given list of list of list etc of integers
    write recursive function that will accept as argument target list
    and return sum of all integers inside it
    Input: [[[[1, 4, 5], [[6, 9],[[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]
    Output: Target sum = 72
"""

input_l = [[[[1, 4, 5], [[6, 9], [[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]


def get_sum(target_list):
    """
    Recursive function that accepts target list as argument.

    Args:
        target_list (type == list): should contain only lists

    Returns:
        total
    """
    total = 0
    for el in target_list:
        total += get_sum(el) if type(el) == list else el
    return total


print(f'Target sum = {get_sum(input_l)}')
