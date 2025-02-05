# file handling and exception management
file=open('test.txt','w')
file.close()
file=open('test.txt','w')
file.close()
# 1._r-read
# 2.w-write
# 3.a-append
# 4.r+-read and write
with open('test.txt','w')as file:
    file.write('hello')
    file.write('world')
    file.write('\n')
    file.write("This is a file handling test case")
    file.close()
    # reading an entire file
with open ('test.txt','r') as file:
    data=file.read()
    print(data)
# reading line by line
with open ('test.txt','r') as file:
    for line in file:
        print(line.strip())
# Reading specific number of character
with open ('test.txt','r') as file:
    data=file.read(10)
    print(data)
# append to a file
with open ('test.txt','a') as file:
    file.write('this line is appended')