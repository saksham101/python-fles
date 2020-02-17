a=int(input("enter first value"))
b=int(input("enter second value"))
m=a
n=b
print("value of first variable originally",a)
print("value of second variable originally",b)
t=a
a=b
b=t
print("After swappin using temporary variable - ")
print("value of first variable=",a)
print("value of second variable=",b)

print("value of first variable originally",m)
print("value of second variable originally",n)
m,n=n,m 
print("After swappin without using temporary variable - ")
print("value of first variable=",m)
print("value of second variable=",n)
