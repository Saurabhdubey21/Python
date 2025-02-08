def fact(num):
    if num==0:
        return 1
    else:
        return num * fact(num-1)
n=int(input("enter a number: "))
f=fact(n)
print(f"the factorial of {n} is {f}")