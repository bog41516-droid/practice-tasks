# task1/solution.py
def sum_neg_between_max_min(arr):
  
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
    # Примеры тестов
    test_arrays = [
        [5, -2, 8, -3, 1, -7, 4],   # ожидаемый результат -3
        [1, 2, 3],                   # 0
        [-5, -10, -2, 0, 4],         # 0 (нет отриц. между?)
        [0, -10, 5, -3, 2],          # -10
    ]
    for arr in test_arrays:
        print(f"{arr} -> {sum_neg_between_max_min(arr)}")
