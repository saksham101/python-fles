y= int(input("Please Enter the Year Number you wish: "))

if ((y%400 == 0)or((y%4 == 0)and(y%100 != 0))):
    print("%d is a Leap Year" %y)
else:
    print("%d is Not the Leap Year" %y)
