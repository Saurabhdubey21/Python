#write a programme to calculate the square of all number in a list
from functools import reduce
num_list=[34,43,56,65,34,23,123]
square_list=list(map(lambda x:x**2,num_list))
print(square_list)
total_sum=reduce(lambda x,y:x+y,square_list)
print(total_sum)