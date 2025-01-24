#electricity bill
units=int(input("Enter the number of units:"))
if units<=100:
    print("Electricity bill is:",units*1.5)
else:
    print("Electricity bill is:",(100*1.5)+(units-100)*2.5)
    if units>500:
        print("Electricity bill is:",(100*1.5)+(400*2.5)+(units-500)*4)
        