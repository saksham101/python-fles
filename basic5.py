num = input("enter the number to e checked =")
c=0
for x in num :
  c+=1
sum = 0
while num>=0 :
    num = float(num)
    num2 = num
    r = num%10
    sum+=pow(r,c)
    num/=10
if sum == num2 :
  print("the number is armstrong number")
else :
  print("the number is not armstrong")
