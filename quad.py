import cmath
a = int(input("enter first value"))
b = int(input("enter second value"))
c = int(input("enter third value"))
d = (b**2) - (4*a*c)
r1 = (-b-cmath.sqrt(d))/(2*a)
r2 = (-b+cmath.sqrt(d))/(2*a)
print('The first root',r1)
print('The second root',r2)
