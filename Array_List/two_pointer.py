arr = [3, 1, 4, 1, 5, 9, 2, 6]


def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return (left, right)
        elif s < target:
            left += 1
        else:
            right -= 1
    return None


print(two_sum_sorted(arr, 5))
