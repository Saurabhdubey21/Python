from functools import reduce
num_list=[10,5,7,8,9,54,45,6,7,86]
large=reduce(lambda x,y: x if x>y else y, num_list)
print(large)
total_sum= reduce(lambda x,y:x+y,num_list)
print(total_sum)