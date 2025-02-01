## create a function that takes a string of a numbes seperated by comma
# convert it to a list of integer and returns their sum
def sum_of_numbers(s):
    numbers = [int(x) for x in s.split(",")]  
    return sum(numbers)
print(sum_of_numbers("1,2,3,4,5"))