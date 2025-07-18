print("------------- HELLO!, WELCOME TO OUR AIRLINE -------------")
passenger_number = int(input("Enter the number of passengers: "))
base_ticket = int(input("Enter the base ticket price in euros: "))
print("Now you will enter the age for each of the passengers !!!")
sum = 0
index = 1

while index <= passenger_number:
    age = float(input("Enter the age of passenger " + str(index) + ": "))
    price = base_ticket
    if age >= 0 and age <= 8:
        price = base_ticket - base_ticket*0.5
    elif age >= 9  and age <= 14:
        price = base_ticket - base_ticket*0.3
    elif age >= 15 and age <= 18:
        price = base_ticket - base_ticket*0.3
    elif age >= 19 and age <= 23:
        price = base_ticket - base_ticket*0.3
    elif age >= 60 and age <= 100:
        price = base_ticket - base_ticket*0.3
    sum += price
    index += 1

print("Total price is: " + str(sum) + " euros")
