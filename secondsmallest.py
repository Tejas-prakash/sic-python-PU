x=int(input('enter 1st Number:'))
y=int(input('enter 2nd Number:'))
z=int(input('enter 3rd Number:'))
if x>y and x<z:
    print(x,'is the second smallest number')
if y>x and y<z:
    print(y,'is the second smallest number')
if z>y and z<x:
    print(z,'is the second smallest number')