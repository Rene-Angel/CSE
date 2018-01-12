# Rene-Angel Jaime
import random

cash = 15
d1 = (random.randint(1, 6))
d2 = (random.randint(1, 6))
dtotal = d1 + d2
print("Dice:" + "%s" % dtotal)

while cash > 0:
    cash = cash - 1
    print(cash)
if dtotal == 7:
    cash = cash + 5
    print("Cash:" + "%s" % cash)
