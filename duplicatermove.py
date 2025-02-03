# create a programme to remove duplicates from a list using a set
numbers={1,2,3,4,5,6,7,8,9,1,2,34,34,5,6,7,84,3,5,6,3,545}
unique_number=[]
seen=set()
for i in numbers:
    if i not in seen:
        unique_number.append(i)
        seen.add(i) 
print(unique_number)