# palidrone number
n=int(input("Enter a number: "))
no=n
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
if no==rev:
    print("The number is palindrome!")
else:
    print("The number isn't palindrome!")