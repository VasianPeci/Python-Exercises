import math

a = float(input("Enter number a: "))
b = float(input("Enter number b: "))
c = float(input("Enter number c: "))
d = b*b - 4*a*c

if d>0:
    r1 = (-b + math.sqrt(d))/(2*a)
    r2 = (-b - math.sqrt(d))/(2*a)
    print("r1 = "+str(r1)+", r2 = "+str(r2))
else:
    if d==0:
        r1 = -b/(2*a)
        r2 = r1
        print("r1 = "+str(r1)+", r2 = "+str(r2))
    else:
        print("Roots are imaginary.")
