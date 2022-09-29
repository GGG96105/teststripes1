def liar(a, player_list, wild_card):
    checked_hand = []
    to_be_checked = []

    for player in player_list:
        for n in player.hand:
            to_be_checked.append(n)
    if wild_card == 1:
        for i in to_be_checked:
            if i == 1:
                checked_hand.append(a.current_bet[0])
            else:
                checked_hand.append(i)
    else:
        for i in to_be_checked:
            checked_hand.append(i)
    if a.current_bet[1] <= checked_hand.count(a.current_bet[0]):
        return 0
        # if telling the truth
    else:
        return 1
        # if lying


def player_creation(number_of_players, class_used, player_list):
    for i in range(number_of_players):
        globals()["w" + str(i)] = class_used(f'Player {i + 1}', i + 1)
        player_list.append(globals()["w" + str(i)])


def betting_tab():
    if str(input("Is the last bitter laying? y/n ")) == "y":
        # liar
        return 0
    else:
        # wants to bet
        return 1
