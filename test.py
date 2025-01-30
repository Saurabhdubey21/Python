import mymodule
print(mymodule.add(3,4)) 
print(mymodule.sub(5,4)) 
print(mymodule.mul(5,4)) 
from mymodule import add,PI
num1=int(input("Enter any number:"))
num2=int(input("Enter any number:"))
print(mymodule.add(num1,num2))
print(PI)