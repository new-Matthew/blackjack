import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_hand = []
computer_hand = []

def deal_card():
    take_another_card = random.choice(cards)
    return take_another_card

for _ in range(2):
    user_hand.append(deal_card())
    computer_hand.append(deal_card())

print(user_hand)
print(computer_hand)
