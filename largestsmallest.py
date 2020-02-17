no1 = float(input("Enter first number "))
no2 = float(input("Enter second number "))
 
if (no1 > no2):
   largest = no1
else:
   largest = no2
print("The largest number out of two numbers is",largest)

n1 = float(input("Enter first number "))
n2 = float(input("Enter second number "))
n3 = float(input("Enter third number "))
 
if (n1 < n2) and (n1 < n3):
   s = n1
elif (n2 < n1) and (n2 < n3):
   s = n2
else:
   s = n3
 
print("The smallest number out of three numbers is",s)
