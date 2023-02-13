# Casino with multiple types of games

class Casino:
    def __init__(self, money: int, coins=0):
        self._money = money
        self._coins = coins

    @property
    def coins(self):
        return self._coins

    @property
    def money(self):
        return self._money

    @coins.setter
    def coins(self, value):
        self._coins = value

    @money.setter
    def money(self, value):
        self._money = value

    def exchange_money_to_coins(self):
        money_to_exchange = int(input("How much money do you want to exchange: "))
        if self._money >= money_to_exchange:
            self.coins += money_to_exchange
        else:
            print("Sorry not enough money")

    def exchange_coins_to_money(self):
        coins_to_exchange = int(input("How many coins do you want to exchange: "))
        if self.coins <= coins_to_exchange:
            self.money += coins_to_exchange
        else:
            print("Sorry not enough coins")


class Games(Casino):
    def __init__(self, money, coins=0):
        super().__init__(money, coins)

    def black_jack(self):
        print("Welcome to Black Jack the minimum to play is 5 coins")
        if self.coins >= 5:
            self.coins -= 5
            print("You can play")


# TEST
user_1 = Games(45)
user_1.exchange_money_to_coins()
print(user_1.coins)

user_1.black_jack()
print(user_1.coins)
