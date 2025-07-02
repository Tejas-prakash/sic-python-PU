n, x, y = map(int, input().split())
arr = list(map(int, input().split()))

count = 0

for p in range(1, 1001):
    more = 0  
    less = 0  
    for num in arr:
        if num > p:
            more += 1
        elif num < p:
            less += 1

    if more == x and less == y:
        count += 1

print(count)
