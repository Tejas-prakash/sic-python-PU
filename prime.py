x=input('enter a number: ')
prime=[2,3,5,7]
count=0
for i in x:
    if int(i) in prime:
        count+=1
print(count, 'number of prime numbers ')
