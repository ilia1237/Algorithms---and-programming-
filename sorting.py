def quicksort(arr: list[int]) -> list[int]:
    """
    Сортування QuickSort (Швидке сортування).
    Часова складність: O(n log n) у середньому, O(n²) у найгіршому випадку.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def bubble_sort(arr: list[int]) -> list[int]:
    """
    Сортування бульбашкою (Bubble Sort).
    Часова складність: O(n²).
    """
    a = arr.copy()
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a
