import random

year = random.randint(1500,2020)

print("The year generated is: "+str(year))

if ((year > 1548) and (year % 400 == 0  or (year % 4 == 0 and year % 100 != 0))):
    print(str(year)+" is a leap year.")
else:
    print(str(year)+" is not a leap year.")
