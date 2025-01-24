#student marksheet
Name=input("Enter your name:")
print(Name)
marks=int(input("Enter your marks:"))
if marks>=90:
    print("Grade A+")
else:
    if marks>=80:
        print("Grade A")
    else:
        if marks>=70:
            print("Grade B")
        else:
            if marks>=60:
                print("Grade C")
            else:
                if marks>=50:
                    print("Grade D")
                else:
                    if marks>=40:
                        print("Grade E")
                    else:
                        print("Fail")