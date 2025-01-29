def is_prime(number):
    if number < 2:
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
        return True
num_list=[2,3,4,5,6,7,8,9,11,24,23,56,67,86,89,97,93,119,131]
prime_number_list=list(filter(is_prime,num_list))
print("prime numbers list:",prime_number_list)