n=int(input("enter a number: "))
m=n
rev=0
 
while m!= 0:
	rev=(rev * 10)+(m%10)
	m=m//10
 
if n==rev:
	print("number is palindrome")
else:
	print("number is not palindrome")

#OUTPUT:
	
#enter a number: 121
#number is palindrome
	
#enter a number: 233
#number is not palindrome	
