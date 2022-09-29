import random


class Basic:

    dice_amount = 5
    current_bet = []

    def __init__(self, name, spot):
        self.name = name
        self.spot = spot
        self.hand = []
        self.create_hand()

    def get_name(self):
        return self.name

    def get_spot(self):
        return self.spot

    def create_hand(self):
        self.hand = []
        i = 0
        while i < self.dice_amount:
            self.hand.append(random.randint(1, 6))
            i += 1

    def lose_dice(self):
        self.dice_amount -= 1

    def get_hand(self):
        for i in self.hand:
            print(i, end=", ")
        print()

    def get_dice(self):
        print(self.dice_amount)

    def get_bet(self):
        for i in self.current_bet:
            print(i, end=", ")


class Player(Basic):
    def bet(self):
        self.current_bet = []
        self.current_bet.append(int(input(f"{self.name} set a face value for your bet: ")))
        self.current_bet.append(int(input(f"{self.name} set a number value to your bet: ")))


class Bot(Basic):
    def __int__(self,  previous_bet):
        self.previous_bet = previous_bet

    def bet(self):
        self.current_bet = []
        # if self.previous_bet.hand[0] < 6:
        #     n = self.previous_bet.hand[0] + 1
        # else:
        #     n = self.previous_bet.hand[0]
        self.current_bet.append(1)
        self.current_bet.append(1)
