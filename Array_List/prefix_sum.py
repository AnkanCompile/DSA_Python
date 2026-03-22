arr = [3, 1, 4, 1, 5, 9, 2, 6]

def prefix_sum(arr):
    n = len(arr)
    pref_sum = [0] * n
    pref_sum[0] = arr[0]
    for i in range(1, n):
        pref_sum[i] = pref_sum[i - 1] + arr[i]
    return pref_sum

print(prefix_sum(arr))
