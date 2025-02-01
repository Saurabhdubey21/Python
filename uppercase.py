# write a programe to convert list of strings to upper case and remove duplicate using list comperehensions
input_list = ["apple", "banana", "apple", "cherry", "banana"]
output_list = [item.upper() for item in set(input_list)]    
print(output_list)