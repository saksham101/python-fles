n=int(input("Enter the no. of elements you want = "))
a=[]
for i in range(0,n):
 a.append(int(input("Enter array element")))

for x in range(0,n): 
    print(a[x],end=" ")

#OUTPUT:
# Enter the no. of elements you want = 5
# Enter array element 1
# Enter array element 2
# Enter array element 3
# Enter array element 4
# Enter array element 5
# 1 2 3 4 5 
