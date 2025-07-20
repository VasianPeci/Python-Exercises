int_list = str(input("Enter a list of integers separated by spaces: ")).split()
int_list = [int(x) for x in int_list]

new_list = []

def zigzagOrder():
    if len(int_list) == 1 or len(int_list) == 0:
        new_list = int_list
        return new_list

    if len(int_list) == 2:
        new_list = sorted(int_list)
        return new_list

    new_list = sorted(int_list)
    if len(new_list) % 2 == 0:
        for i in range(1, len(new_list)-1, 2):
            temp = new_list[i]
            new_list[i] = new_list[i+1]
            new_list[i+1] = temp
        return new_list
    else:
        for i in range(1, len(new_list), 2):
            temp = new_list[i]
            new_list[i] = new_list[i+1]
            new_list[i+1] = temp
        return new_list

print(f"Zigzag order: {zigzagOrder()}")
