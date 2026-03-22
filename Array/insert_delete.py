arr = [3, 1, 4, 1, 5, 9, 2, 6]

operations = [
    lambda: arr.append(7),
    lambda: arr.insert(2, 99),
    lambda: arr.remove(99),
    lambda: arr.pop(),
    lambda: arr.pop(0),
]

for x in operations:
    x()
    print(arr)
