import random
from matplotlib import pyplot as plt

class Trader():
    def __init__(self, balance):
        self.balance = balance
    def __lt__(self, other):
        return self.balance < other.balance

traders = []
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
        faceoff(traders)

x_data = []
y_data = []

def process_data():
    global x_data
    global y_data
    traders.sort()

    for t in traders:
        if t.balance not in x_data:
            x_data.append(t.balance)
            y_data.append(1)
        else:
            y_data[-1] += 1

def main(t, tb, gens):
    generate_traders(trader_amount=t, trader_balance=tb)
    generations(repetitons=gens)
    process_data()
    plt.bar(x_data, y_data, width=0.8, bottom=None, align='center')
    plt.show()

main(
    t = 10,    # Traders
    tb = 1,    # Trader Balance
    gens = 100 # Trade rounds 
    )import random
from matplotlib import pyplot as plt

class Trader():
    def __init__(self, balance):
        self.balance = balance
    def __lt__(self, other):
        return self.balance < other.balance

traders = []
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
        faceoff(traders)

x_data = []
y_data = []

def process_data():
    global x_data
    global y_data
    traders.sort()

    for t in traders:
        if t.balance not in x_data:
            x_data.append(t.balance)
            y_data.append(1)
        else:
            y_data[-1] += 1

def main(t, tb, gens):
    generate_traders(trader_amount=t, trader_balance=tb)
    generations(repetitons=gens)
    process_data()
    plt.bar(x_data, y_data, width=0.8, bottom=None, align='center')
    plt.show()

main(
    t = 10,    # Traders
    tb = 1,    # Trader Balance
    gens = 100 # Trade rounds 
    )
