n=int(input("Enter the no. of terms required"))
f=0                                     
sum=1 
if n<=0:
    print("The requested series is",f)
else:
    print(f,sum,end=" ")
    for a in range(2,n):
        next=f+sum                          
        print(next,end=" ")
        f=sum
        sum=next

#OUTPUT : Enter the no. of terms required 5
#         0 1 1 2 3 
        
