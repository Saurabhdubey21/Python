#use of non variable
x=20
def sum():
    y=20
    def f():
        nonlocal y
        y +=10
        print(f"nonlocal y:{y}")
    f()
    print(f"global x:{x}")
sum()