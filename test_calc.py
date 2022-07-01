from main import calculate_sum


def test_empty_list():
    some_list = []

    assert calculate_sum(some_list) == 0


def test_incorrect_list():
    some_list = ['q', 'w', 'e']

    assert calculate_sum(some_list) == 0


def test_correct_list():
    some_list = [1, 2, 3, 4, 5]

    assert calculate_sum(some_list) == 3
