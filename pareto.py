import random
from matplotlib import pyplot as plt

plt.ion()
traders = []

class Trader():
    def __init__(self, balance):
        self.balance = balance
    def __lt__(self, other):
        return self.balance < other.balance

def generate_traders(trader_amount, trader_balance):
    for x in range(trader_amount):
        t = Trader(balance=trader_balance)
        traders.append(t)

def faceoff(traders=traders):
    for trader in traders:
        if trader.balance >= 1:
            trader.balance -= 1
            while True:
                receiver = random.choice(traders)
                if receiver.balance >= 1:
                    receiver.balance += 1
                    break
                    
def generations(repetitons):
    for generation in range(repetitons):
        data = {}
        faceoff(traders)
        traders.sort()
        for t in traders:
            if t.balance not in data.keys():
                data[t.balance] = 1
            else:
                data[t.balance] += 1
                
        plt.cla()
        plt.bar(data.keys(), data.values(), width=0.8, bottom=None, align='center')
        plt.pause(0.1)
        plt.show()

generate_traders(trader_amount=100, trader_balance=5)
generations(repetitons=100)
