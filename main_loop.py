from player_classes import Player, Bot
from functions_tab import liar, player_creation, betting_tab

player_list = []
player_creation(5, Player, player_list)
last_bitter = 0
last_bet = [0, 0]
wild_card = 0

while True:
    for person in player_list:
        person.create_hand()
        print(last_bet)
        person.get_hand()
        if betting_tab() == 0:
            if liar(player_list[last_bitter], player_list, wild_card) == 1:
                player_list[last_bitter].lose_dice()
                print(f"{player_list[last_bitter].name} lost a dice! ")
                break
            else:
                person.lose_dice()
                print(f"{person.name} lost a dice! ")
                break
        else:
            person.bet()
            last_bet = person.current_bet
            if last_bitter <= len(player_list):
                last_bitter = 0
            else:
                last_bitter += 1
