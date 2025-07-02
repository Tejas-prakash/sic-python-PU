
def binary_search(arr, number):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == number:
            return mid  
        elif arr[mid] < number:
            low = mid + 1
        else:
            high = mid - 1

    return -1 

arr = [10, 20, 30, 40, 50, 60]
number = int(input("Enter number to search: "))

index = binary_search(arr, number)

if index != -1:
    print("Found at index", index)
else:
    print("Not found")
