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


def chunks_generator(range_value, chunks_size):
    """
    Generate chunked list according to entered range value and chunk size.

    Args:
        range_value (int):  Limit for the list to be chunked
        chunks_size (int): The chunk size
    Yields:
        list(range_value[:chunks_size]): list only for chunk
    Returns:
        None
    """
    while range_value:
        yield list(range_value[:chunks_size])
        range_value = range_value[chunks_size:]


range_value = int(input('Please, enter range value: '))
chunks_size = int(input('Please, enter chunk size: '))

print(*list(chunks_generator(range(range_value), chunks_size)), sep='\n')
