def binary_search(arr: list[int], target: int) -> int:
    """
    Бінарний пошук у відсортованому масиві.
    Повертає індекс елемента або -1, якщо елемент не знайдено.
    Часова складність: O(log n).
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1
