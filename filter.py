# wap to find all numbers divisible by 3 and 5 in a list
num_list=[5,3,6,7,90,75,45,3,4,24]
div_3_list=list(map(lambda x:x%3==0,num_list))
print(div_3_list)
div_5_list=list(map(lambda y:y%5==0,num_list))
print(div_5_list)
div_3_and_5=list(filter(lambda x:x%3==0 and x%5==0,num_list))
print("the number divisible by 3 and 5:",div_3_and_5)