from collections import deque


def sliding_window_max(arr, k):
    dq, res = deque(), []
    for i, v in enumerate(arr):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and arr[dq[-1]] < v:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(arr[dq[0]])
    return res


arr = [3, 1, 4, 1, 5, 9, 2, 6]
print(sliding_window_max(arr, 5))
