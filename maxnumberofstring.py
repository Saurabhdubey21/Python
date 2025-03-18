#find maximum number of string in a list
def maxnumberofstring(list1):
    result = 0
    for i in list1:
        if int(i) > result:
            result = int(i)
    return result
list1 = input("Enter the list of number: ").split()
print(maxnumberofstring(list1))
