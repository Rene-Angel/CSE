# Rene-Angel Jaime
import random
cash = 15

while cash > 0:
    d1 = (random.randint(1, 6))
    d2 = (random.randint(1, 6))
    total = d1 + d2
    print("Rolled: %s" % total)
    print("Cash: %s" % cash)

    if d1 + d2 == 7:
        cash += 4
        print(cash)
    else:
        cash -= 1
        print(cash)