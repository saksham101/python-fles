nO = int(input("Enter a number: "))
s = 0
t = nO
while t > 0:
   d = t % 10
   s += d ** 3
   t //= 10
if nO == s:
   print(nO,"is an Armstrong number")
else:
   print(nO,"is not an Armstrong number")

#Enter a number: 153
#153 is an Armstrong number
   
#Enter a number: 413
#413 is not an Armstrong number   
