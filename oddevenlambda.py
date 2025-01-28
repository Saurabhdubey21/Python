#odd even by lamda
num=[1,2,3,4,5,6,7,8,9]
def is_even(n):
    if n%2==0:
        return True
even_num = filter(is_even,num)
even_num_list =list(even_num)
print(even_num_list)