y=int(input('enter Year: '))
if (y%4==0 and y%100!=0)or (y%400==0):
    print('Leap year')