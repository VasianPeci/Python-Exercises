a = float(input("Enter number a: "))
b = float(input("Enter number b: "))
c = float(input("Enter number c: "))

if(a>b):
    if(a>c):
        print(a)
    else:
        print(c)
else:
    if(b>c):
        print(b)
    else:
        print(c)
