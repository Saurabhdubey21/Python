#print(even_num_list)
num=[1,2,3,4,5,6,7,8,9]
even_num = filter(lambda x: x%2==0,num)
even_num_list=list(even_num)
print(even_num_list)