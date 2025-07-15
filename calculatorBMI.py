weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight/(height*height)

if(bmi < 18.5):
    print("Your weight status is Underweight.")
elif(18.5 <= bmi < 25):
    print("Your weight status is Normal.")
elif(25 <= bmi < 30):
    print("Your weight status is Overweight.")
else:
    print("Your weight status is Obese.")
