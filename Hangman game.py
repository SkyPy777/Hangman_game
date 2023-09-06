
import random

words = ["python", "hangman", "programming", "challenge", "guess"]
chosen_word = random.choice(words)
guessed_letters = []

print("Welcome to Hangman!")
print(words)

while True:
    display_word = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord to guess:", display_word)

    if display_word == chosen_word:
        print("\nCongratulations! You've guessed the word:", chosen_word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.") 
        continue

    guessed_letters.append(guess)

print("\nThanks for playing Hangman! Goodbye.")



