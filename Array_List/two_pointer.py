arr = [3, 1, 4, 1, 5, 9, 2, 6]

def two_sum_sorted(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        s = arr[l] + arr[r]
        if s == target: return (l, r)
        elif s < target: l += 1
        else: r -= 1
    return None

print(two_sum_sorted(arr, 5))
