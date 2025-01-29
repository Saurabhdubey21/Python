# write a programme to find negative number from a list
num_list=[34,45,6,-6,-8,-45,0,-6]
negative_num=list(filter(lambda x: x<0,num_list))
print(negative_num)