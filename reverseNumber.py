import itertools

for i in itertools.cycle([1,2,3]):
    input_number = int(input("Enter a positive number with a minimum of 3 digits: "))
    if input_number/100 >= 1:
        break

reversed_number = [""]*len(str(input_number))

for i in range(0, len(str(input_number))):
    reversed_number[len(str(input_number))-1-i] = str(input_number)[i]

print("The reversed number is: " + "".join(reversed_number))
