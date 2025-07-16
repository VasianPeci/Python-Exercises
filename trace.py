a = int(input("Enter a whole number: "))
b = int(input("Enter a whole number: "))

if(a+b) % 3 == 0:
    print("Branch 1")
else:
    print("Branch 2")

a = a*2
b = b*3

if(a+b) % 3 == 0:
    print("Branch 3")
else:
    print("Branch 4")

# if a = 5 and b = 4, then the code will print "Branch 1 \n Branch 4"
