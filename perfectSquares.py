perfect_squares = []

for i in range(50, 101):
    for j in range(1,50):
        if j*j == i:
            perfect_squares.append(str(i))

print("Perfect squares are: " + " ".join(perfect_squares))
