
n = int(input("Enter number of oranges: "))

oranges = input("Enter orange sizes: ").split()
oranges = [int(size) for size in oranges]

pivot = oranges[-1]
k = 0

for i in range(n - 1):
    if oranges[i] <= pivot:
        oranges[i], oranges[k] = oranges[k], oranges[i]
        k += 1

oranges[k], oranges[n - 1] = oranges[n - 1], oranges[k]

print("Partitioned oranges:", *oranges)

