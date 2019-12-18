
arr = [1, 5, 0, 4, 7, 0, 0, 6, 0]
index = 0

for i, el in enumerate(arr):
    if el != 0:
        arr[index], arr[i] = arr[i], arr[index]
        index += 1

print(arr)
