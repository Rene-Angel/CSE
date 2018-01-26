import random
import string
"""
Rene-Angel Jaime
A general guide for Hangman
1. Make a word bank - 10 items
2. Pick a random item from the list
3. Add a guess to the list of letters guessed
4. Reveal letters already guessed
5. Create the win condition
"""
word_bank = ["Batman", "HarleyQuinn", "Supergirl", "BlackAdam", "Atrocitus", "Aquaman", "BlueBeetle",
             "WonderWoman", "BlackCanary", "GreenLantern"]
letters_guessed = []
guess = " "
guesses = 10
word = random.choice(word_bank)
correct_letters = list(word)

while guesses > 0 != quit:

    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(output)

    guess = input("Guess a letter: ")
    print("Guesses Left: %s" % guesses)
    letters_guessed.append(guess)
    print(" ".join(letters_guessed))

if guess == correct_letters:
        guesses += 0

if guess != correct_letters:
        guesses -= 1
