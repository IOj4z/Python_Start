import random


# coin = random.choice(['heads', "tails"])
# coin = random.randint(1,10)
# print(coin)

cards = ["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)
