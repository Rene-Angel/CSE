import random
"""
Rene-Angel Jaime
A general guide for Hangman
1. Make a word bank - 10 items
2. Pick a random item from the list
3. Add a guess to the list of letters guessed
4. Reveal letters already guessed
5. Create the win condition
"""
word_bank = ["batman", "harleyquinn", "supergirl", "blackadam", "atrocitus", "aquaman", "bluebeetle",
             "wonderwoman", "blackcanary", "greenlantern"]
letters_guessed = []
guess = " "
guesses = 11
word = random.choice(word_bank)
correct_letters = list(word)

while guesses >= 2 != quit:
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(" ".join(list(output)))
    if guess not in word:
        guesses -= 1
        print("Guesses Left: %s" % guesses)
    else:
        print("Guesses Left: %s" % guesses)
    guess = input("Guess a letter: ")
    letters_guessed.append(guess)
    print(" ".join(letters_guessed))

if output == word:
    print("You Win! :)")
    exit(0)
if guesses == 0:
    print("You Lose! :(")
    exit(0)
