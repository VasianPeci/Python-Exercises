word = str(input("Enter a word to be checked for being palindrome: "))

reversed_word = [""]*len(word)

for i in range(0, len(reversed_word)):
    reversed_word[len(reversed_word)-1-i] = word.lower()[i]

if word.lower() == "".join(reversed_word):
    print(word + " is a palindrome!")
else:
    print(word + " is not a palindrome!")
