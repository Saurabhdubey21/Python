age=[10,20,30,32,12,34,54,23,13]
def my_function(age1):
    if age1>=18:
        return True
    else:
        return False
adults=list(filter(my_function,age))
for x in adults:
    print(x,end=" ")
adults=list(filter(lambda x :x>18,age))
print(adults)