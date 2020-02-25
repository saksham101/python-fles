num = input("enter a number to be checked for prime number")
num = int(num)
i = num
j=1
c=0
while j<=i :
  if i%j==0 :
    c+=1
  j+=1
if c==2 :
    print("entered number is prime")
else :
    print("not prime")
