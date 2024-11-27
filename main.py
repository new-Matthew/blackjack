import random
from time import sleep
print("Bem Vindo Ao Jogo Blackjack!!")
def play_game():
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
            cards.append(1)
            
        return sum(cards)

    def compare(u_score, c_score):
        if u_score == 0:
            return "Você venceu com um Blackjack!"
        elif c_score == 0:
            return "Você perdeu o oponente obteve um Blackjack!"
        elif u_score > 21:
            return "Você perdeu!"
        elif c_score > 21:
            return "Você venceu!"
        elif u_score > c_score:
            return "Você venceu"
        elif c_score == u_score:
            return "Empate!"
        else:
            return "Você perdeu!"

    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)

        print("--------------------------------------------------------------------")
        print(f"Sua mão é: {user_hand} sua pontuação é: {user_score} ")
        print(f"A primeira carta da mão do oponente é: {computer_hand[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            is_game_over = True
        else:    
            ask_draw_card = input("Quer puxar uma carta? digite 's' ou 'n' ")
            if ask_draw_card == 's':
                user_hand.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"Sua mão final é: {user_hand} sua pontuação final é: {user_score}")
    print(f"A mão final do oponente é: {computer_hand} a pontuação final do oponente é: {computer_score}")
    score_of_winner = compare(user_score, computer_score)
    print(score_of_winner)

while input("Você quer jogar Blackjack? 's' para sim e 'n' para não ") == 's':
    play_game()
    sleep(5)
    print("\n" * 20)