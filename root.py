#find roots of a quadratic equation
import math
a=float(input("Enter the cofficient of x^2: "))
b=float(input("Enter the cofficient of x: "))
c=float(input("Enter the constant term: "))
d=(b**2-(4*a*c))
root1=(-b+math.sqrt(d))/(2*a)
root2=(-b-math.sqrt(d))/(2*a)
print("The roots of the equation are: ",root1,root2)
if d>0:
    print("The roots are real and distinct")
else:
    if d==0:
        print("The roots are real and equal")
    else:
        print("The roots are imaginary")