#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль для вычисления суммы отрицательных элементов между максимумом и минимумом.
"""

from typing import List, Union

def sum_neg_between_max_min(arr: List[Union[int, float]]) -> Union[int, float]:
    """
    Вычисляет сумму отрицательных элементов, расположенных между максимальным
    и минимальным элементами массива (не включая сами экстремумы).

    Аргументы:
        arr (list of int/float): список чисел.

    Возвращает:
        int/float: сумма отрицательных элементов в интервале.
                   Если массив содержит менее 2 элементов, возвращает 0.

    Примеры:
        >>> sum_neg_between_max_min([5, -2, 8, -3, 1, -7, 4])
        -3
        >>> sum_neg_between_max_min([1, 2, 3])
        0
        >>> sum_neg_between_max_min([-5, -10, -2, 0, 4])
        -2
    """
    if len(arr) < 2:
        return 0

    idx_max = 0
    idx_min = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[idx_max]:
            idx_max = i
        if arr[i] < arr[idx_min]:
            idx_min = i

    left = min(idx_max, idx_min)
    right = max(idx_max, idx_min)

    total = 0
    for i in range(left + 1, right):
        if arr[i] < 0:
            total += arr[i]
    return total


if __name__ == '__main__':
    # Демонстрационные примеры (для быстрой проверки)
    test_arrays = [
        ([5, -2, 8, -3, 1, -7, 4], -3),
        ([1, 2, 3], 0),
        ([-5, -10, -2, 0, 4], -2),   # исправлено: было 0, стало -2
        ([0, -10, 5, -3, 2], -10),
        ([7], 0),
        ([], 0),
    ]
    for arr, expected in test_arrays:
        result = sum_neg_between_max_min(arr)
        print(f"{arr} -> {result} (ожидалось {expected})")
        assert result == expected, f"Ошибка: {arr} дало {result}, а должно {expected}"
    print("Все демо-тесты пройдены.")
