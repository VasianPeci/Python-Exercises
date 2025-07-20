length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

def calculate_area(length, width):
    return length*width

def calculate_perimeter(length, width):
    return 2*(length+width)

print(f"The area of the rectangle is: {calculate_area(length, width)}")
print(f"The perimeter of the rectangle is: {calculate_perimeter(length, width)}")
