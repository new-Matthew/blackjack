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
    if 11 in cards and score > 21:
        cards.remove(11)
        
    return sum(cards)

is_game_over = False

while not is_game_over:
    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    print(f"Sua mão é: {user_hand} sua pontuação é: {user_score} ")

    print(f"A primeira carta da mão do oponente é: {computer_hand[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
        print("game over!")
        is_game_over = True
    else:
        ask_draw_card = input("Quer puxar uma carta? digite 's' ou 'n' ")
        if ask_draw_card == 's':
            user_hand.append(deal_card())
        else:
            is_game_over = True