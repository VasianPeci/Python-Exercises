drivingDistance = float(input("Enter the driving distance in km: "))
literPerKm = float(input("How many liters does your vehicle consumes for 100km: "))/100
price = float(input("Enter price per liter in LEK: "))

cost = drivingDistance*literPerKm*price

print("Total Driving Cost is: "+str(cost))
