num1 = input("enter the number from which you wanna print the prime numbers")
num2 = input("enter the number upto which you wanna print the prime numbers")
num1 = int(num1)
num2 = int(num2)
i = num1
while i <= num2 :
    j = 1
    c = 0
    while j<=i :
        if i%j==0 :
            c+=1
        j+=1
    if c==2 :
        print(i)
    i+=1
