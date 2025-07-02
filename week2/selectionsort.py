arr = [64, 25, 12, 22, 11]
n = len(arr)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp

print("Sorted array:", arr)
