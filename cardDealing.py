import random

symbols = ['♠', '♣', '♦', '♥', '🃏']
deck_of_cards = []

for i in range(0, 4):
    for j in range(2, 11):
        deck_of_cards.append((j, symbols[i]))
    deck_of_cards.append(('J', symbols[i]))
    deck_of_cards.append(('Q', symbols[i]))
    deck_of_cards.append(('K', symbols[i]))
    deck_of_cards.append(('A', symbols[i]))
deck_of_cards.append(('Black Joker', symbols[4]))
deck_of_cards.append(('Red Joker', symbols[4]))

random.shuffle(deck_of_cards)

first_player = []
second_player = []
third_player = []
fourth_player = []

count = 1

for card in deck_of_cards:
    if count == 5:
        count = 1

    if count == 1:
        first_player.append(card)
    elif count == 2:
        second_player.append(card)
    elif count == 3:
        third_player.append(card)
    else: fourth_player.append(card)

    count += 1

print(f"First player: {first_player}")
print(f"Second player: {second_player}")
print(f"Third player: {third_player}")
print(f"Fourth player: {fourth_player}")

players = [first_player, second_player, third_player, fourth_player]

for i, player in enumerate(players):
    hasCardGreaterThan10 = False
    for card in player:
        if not isinstance(card[0], int):
            hasCardGreaterThan10 = True
            break
    if not hasCardGreaterThan10:
        print(f"Player {i+1}: Do you want to terminate the game or continue?")
