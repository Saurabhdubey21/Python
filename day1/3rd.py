import math
a=int(input("Enter first side of triangle:"))
b=int(input("Enter second sidee of triangle:"))
c=int(input("enter third side of triangle:"))
s=(a+b+c)/2
print(s)
s1=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle:",s1)