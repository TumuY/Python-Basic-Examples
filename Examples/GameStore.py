class Account():
    def __init__(self,id,pasw):
        self.id = id
        self.pasw = pasw
        self.starter()

    @property
    def balance(self):
        return self.accountbalance

    @balance.setter
    def balance(self, value):
        self.accountbalance += value

    def starter(self):
        self.accountbalance = 0



class Store():
    games= []
    def __init__(self,storename):
        self.storename = storename

    def AddtoList(self, game, price):
        self.game = game
        self.price = price
        Store.games.append((self.game,self.price))

    @classmethod
    def BuyGame(cls, account,):
        a = input("Game : ")
        for game in Store.games:
            if a == game[0]:
                if account.accountbalance >= game[1]:
                    account.accountbalance = account.accountbalance - game[1]
                    print("You succesfully buyed the game : {}, your new balance is {}".format(game[0],account.accountbalance))
                else:
                    print("Insufficient balance")
            else:
                print("The game you are looking for is not available.")
