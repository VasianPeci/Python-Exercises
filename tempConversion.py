celsius = float(input("Enter the temperature in Celsius: "))

def convert_to_fahrenheit(celsius):
    return (celsius*9/5)+32

def display_temperature(fahrenheit):
    print(f"The temperature in Fahrenheit is: {fahrenheit}°F")

display_temperature(convert_to_fahrenheit(celsius))
