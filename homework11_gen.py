"""
Homework11.

Description:
    write generator function that has as input some range value and chunk_size
    produces output as lists with len == chunk size
    Example:
    Call: chunk_generator(range(11), chunk_size=3)
    Output:
    [0, 1, 2]
    [3, 4, 5]
    [6, 7, 8]
    [9, 10]
"""


def chunk_generator(range_value, chunk_size):
    """
    Generate chunked list according to entered range value and chunk size.

    Args:
        range_value (int):  Limit for the list to be chunked
        chunk_size (int): The chunk size

    Yields:
        sliced_list[el:el+chunk_size]: sliced list with [start:end] positions

    Returns:
        None
    """
    sliced_list = list(range(range_value))
#                   start, stop, step
    for el in range(0, len(sliced_list), chunk_size):
        yield sliced_list[el:el + chunk_size]


range_value = int(input('Please, enter range value: '))
chunk_size = int(input('Please, enter chunk size: '))

for chunk in chunk_generator(range_value, chunk_size):
    print(chunk)
