#print resident or not
age=int(input("Enter your age:"))
if age>=18:
    if country=="India":
        print("you are eligible to vote")
    else:
        print("you are resident")
else:
    print("you are not resident")