original_string = "I love coding!"
reversed_string = [""] * len(original_string)
index = len(original_string) - 1

while index >= 0:
    reversed_string[len(original_string) - index - 1] = original_string[index]
    index -= 1

print("Original string: "+original_string)
print("Reversed string: "+"".join(reversed_string))
