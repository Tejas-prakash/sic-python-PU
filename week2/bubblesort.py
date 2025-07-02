arr = [64, 25, 12, 22, 11]
n = len(arr)

for i in range(n):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("Sorted array:", arr)
