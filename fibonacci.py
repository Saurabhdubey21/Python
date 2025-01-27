# fibonacci series
terms=int(input("Enter the number of terms: "))
n1=0
n2=1
counter=0
print("Fibonacci series: ")
while counter<terms:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    counter+=1