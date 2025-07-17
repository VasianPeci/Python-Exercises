import random

round = 1
generated_number = random.randint(20,200)
print(generated_number)

while round <= 7:
    guess = int(input("Guess the number: "))
    if guess == generated_number:
        print("Congratulations! You guessed the correct number!")
        break
    round += 1

if round == 8:
    print("You did not find the correct answer!")
