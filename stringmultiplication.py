#multiplication the element of given string
def stringmultiplication(str1):
    str2 = str1.split()
    result = 1
    for i in str2:
        result = result * int(i)
    return result
str1 = input("Enter the string: ")
print(stringmultiplication(str1))