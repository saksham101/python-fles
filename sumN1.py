n = int(input("Enter the value of n: "))
hold = n
sum = 0
if n <= 0: 
   print("Enter a whole positive number!") 
else: 
   while n > 0:
        sum = sum + n
        n = n - 1;
   print("Sum of first", hold, "natural numbers is: ", sum)
