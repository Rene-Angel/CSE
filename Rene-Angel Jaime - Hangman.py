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
word_bank = ["Batman", "Harley Quinn", "Supergirl", "Black Adam", "Atrocitus", "Aquaman", "Blue Beetle",
             "Wonder Woman", "Black Canary", "Green Lantern"]
letters_guessed = []
# guess =
guesses = 10
str1 = (random.choice(word_bank))
listOne = list(str1)
print(listOne)
# while guesses > 0: