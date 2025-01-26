#
rows=int(input("Enter the number of rows: "))
name=input("Enter the name: ")
count=1
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(name,end=" ")
        count+=1
    print()