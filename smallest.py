x=int(input('enter 1st Number:'))
y=int(input('enter 2nd Number:'))
z=int(input('enter 3rd Number:'))
if x<y:
    if x<z:
        print(x,' is the smallest number')
elif y<x:
    if y<z:
        print(y,' is the smallest number')
elif z<x:
    if z<y:
        print(z,' is the smallest number')