def calculate_sum(list_: list) -> int:
    """Calculates the sum of the two smallest elements of a list.
    Args:
        list_: List of integer values.
    Returns:
        int: Sum of two elements, or one element, or zero.
    """
    if not list_:
        return 0
    if not all(isinstance(elem, int) for elem in list_):
        return 0
    if len(list_) == 1:
        return list_[0]
    list_copy = list_[:]
    first_num = min(list_copy)
    list_copy.remove(first_num)
    second_num = min(list_copy)
    return first_num + second_num


if __name__ == '__main__':
    print(calculate_sum([4, 0, 3, 19, 492, -10, 1]))
