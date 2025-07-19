phone_numbers = {}

def add_contact(name, number):
    phone_numbers[name] = number
    print(f"Added contact: {name} -> {number}\n")

def modify_contact(name, number):
    phone_numbers[name] = number
    print(f"Modified contact: {name} -> {number}\n")

def search_contact(name):
    print(f"{name}'s phone number is {phone_numbers[name]}.\n")

while 1:
    response = str(input("Choose one of these operations:\n1 - Add a new contact\n2 - Modify a saved contact's phone number\n3 - Search for a phone number by name\nq - quit\n"))

    if response == '1':
        name = str(input("\nWrite the name of the contact you want to add: "))
        if name in phone_numbers:
            print(f"{name} is already registered!\n")
            continue
        number = str(input("Write the phone number of the contact you want to add: "))
        add_contact(name, number)
    elif response == '2':
        name = str(input("\nWrite the name of the contact you want to modify: "))
        if name not in phone_numbers:
            print(f"{name} is not registered!\n")
            continue
        number = str(input("Write the phone number of the contact you want to modify: "))
        modify_contact(name, number)
    elif response == '3':
        name = str(input("\nWrite the name of the contact you want to search: "))
        if name not in phone_numbers:
            print(f"Contact '{name}' not found.\n")
            continue
        search_contact(name)
        continue
    elif response.lower() == 'q':
        break
    else:
        print("\nYour response should be 1-3 or q!\n")
        continue

    print(f"Updated Contact List: {phone_numbers}\n")
