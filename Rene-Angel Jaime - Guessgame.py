# Rene-Angel Jaime
# 1) Generate random number
# 2) ake and input (number) form the user
# 3) Compare input to generated number
# 4) Add "higher" and "lower" statements
# 5) Add 5 guesses

import random

guessesTaken = 0

print("Hello! What is your name?")
myName = input()

number = random.randint(1, 50)
print("Well %s, I am thinking of a number between 1 and 50." % (myName))

guess = ''
while guessesTaken < 5 and guess != number:
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    guessesTaken += 1

    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")

if guess == number:
    guessesTaken = str(guessesTaken)
    print("Good job, %s! You guessed my number in %s guesses!" % (myName, guessesTaken))

if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was %s." % (number))