from algorithms.sorting import bubble_sort, quicksort


def test_quicksort():
    sample = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    assert quicksort(sample) == expected
    assert quicksort([]) == []


def test_bubble_sort():
    sample = [5, 1, 4, 2, 8]
    expected = [1, 2, 4, 5, 8]
    assert bubble_sort(sample) == expected
