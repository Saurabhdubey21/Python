# asseration 
num=10
assert num>0,"number must be positive"
try:
    with open("text.txt","r") as file:
        content=file.read()
        words=content.spilt()
        print("words count:",len(words))
except FileNotFoundError:
    print("file not found")
import math
try:
    num1=float(input("Enter the first number:"))
    if num1<0:
        raise ValueError("Cannot calculate square root of a negative number")
    print("The square root of",num1,"is",math.sqrt(num1))
except ValueError as e:
    print("Error:",e)