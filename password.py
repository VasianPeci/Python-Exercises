print("------------Welcome!----------------- ")

password = "pass123"
enterPassword = input("Enter your password: ")

if(enterPassword == ""):
    print("Please enter your password!")

elif (enterPassword == password):
    print("Correct! The password you entered matches the original password.")

else:
    print("Incorrect password!")
