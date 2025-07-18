words = ["Car", "home", "House", "King", "king", "queen", "math", "Coding"]

for i in range(len(words)):
    for j in range(0, len(words)-i-1):
        if words[j] > words[j+1]:
            temp = words[j]
            words[j] = words[j+1]
            words[j+1] = temp
print(words)
