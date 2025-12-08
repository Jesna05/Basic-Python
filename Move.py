def move(arr):
    index = 0
    for num in arr:
        if num != 0:
            arr[index] = num
            index += 1
    while index < len(arr):
        arr[index] = 0
        index += 1

    return arr
arr = [2, 0, 4, 3, 7, 0, 5, 6, 0, 7]
print(move(arr))
