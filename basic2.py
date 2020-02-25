def factorial(num) :
    if(num==0) :
        return 1
    elif(num==1) :
        return 1
    else :
        return num*factorial(num-1)
num = input("enter the number")
num = int(num)
fac = factorial(num)
print("factorial is",fac)
