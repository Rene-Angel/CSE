import string
"""
Rene-Angel Jaime
A general guide for Hangman
1. Make a word bank - 10 items
2. Pick a random item from the list
3. Hide teh word(use *)
4. Reveal letters already guessed
5. Create the win condition
"""

word_bank = ["Batman", "Harley Quinn", "Supergirl", "Black Adam", "Atrocitus", "Aquaman", "Blue Beetle",
             "Wonder Woman", "Black Canary", "Green Lantern"]
# random.shuffle(word_bank)
for item in word_bank:
    print(item)
