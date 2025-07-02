def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    smaller = []
    greater = []

    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            smaller.append(arr[i])
        else:
            greater.append(arr[i])

    return quick_sort(smaller) + [pivot] + quick_sort(greater)

a = [12, 4, 56, 43, 21, 20, 11, 65, 22, 66, 7, 8]
b = [7, 8, 9, 2, 10, 11, 12]
c = [12, 11, 6, 4, 3, 2]

print("Sorted a:", quick_sort(a))
print("Sorted b:", quick_sort(b))
print("Sorted c:", quick_sort(c))
