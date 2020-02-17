m=float(input(" Please Enter the First Value a: "))
n=float(input(" Please Enter the Second Value b: "))
i = 1
while(i<=m and i<=n):
    if(m%i==0 and n%i==0):
        g=i
    i=i + 1
    
print("\nGCD of {0} and {1} = {2}".format(m,n,g))

#OUTPUT:
#Please Enter the First Value a: 8
#Please Enter the Second Value b: 12
#GCD of 8.0 and 12.0 = 4
