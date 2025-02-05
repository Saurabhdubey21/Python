# directive traversal
import os
for root, dirs, files in os.walk(''):
    print("root",root)
    print("dirs",dirs)
    print("files",files)
#  print(10/0)
try:
    num=int(input("Enter a number"))
    result=10/num
    print("result:",result)
except ZeroDivisionError:
    print("Error:Zero division not allowed.")
except ValueError:
    print("Error:Invalid input")
def check_age(age):
    if age < 18:
        raise ValueError('age must be older than 18')
    try:
        age = int(age)
        check_age(age)
    except ValueError as e:
        print("Error:",e)