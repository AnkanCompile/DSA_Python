arr = [3, 1, 4, 1, 5, 9, 2, 6]


def max_subarray_sum(arr, k):
    window = sum(arr[:k])
    best = window
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]
        best = max(best, window)
    return best


print(max_subarray_sum(arr, 5))
