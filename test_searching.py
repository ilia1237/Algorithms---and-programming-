from algorithms.searching import binary_search


def test_binary_search_found():
    data = [10, 20, 30, 40, 50]
    assert binary_search(data, 30) == 2


def test_binary_search_not_found():
    data = [10, 20, 30, 40, 50]
    assert binary_search(data, 99) == -1
