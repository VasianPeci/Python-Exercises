words = {}
sentence = str(input("Enter a sentence: "))
wordlist = sentence.split()
for word in wordlist:
    words[word] = len(word)
print(f"Words and their lengths: {words}")
