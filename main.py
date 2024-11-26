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

def calculate_score(cards):
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0
    if 11 in cards and score > 21: # quando tiver dois Áses
        cards.remove(11)
        
    return sum(cards)

user_score = calculate_score(user_hand)
computer_score = calculate_score(computer_hand)

print(user_hand)
print(user_score)

print(computer_hand)
print(computer_score)