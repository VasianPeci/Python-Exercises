for i in range(10, 0, -1):
    printed_row = [""]*i
    for i in range(0, i):
        printed_row[i] = str(i+1)
    print(" ".join(printed_row))
