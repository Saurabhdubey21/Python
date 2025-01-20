import math
a=float(input("Enter amount:"))
b=float(input("Enter rate:"))
c=int(input("Enter time:"))
d=a*(1+(b/100))**c-a
print("Compound interest:",d)