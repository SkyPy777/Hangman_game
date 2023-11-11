import random

#List of words to be guessed by player randomly
words = ["python", "hangman", "programming", "challenge", "guess"]

#Selecting random words from the list
chosen_word = random.choice(words)

#Keeps track of words guessed by player
guessed_letters = []

#Welcome message
print("Welcome to Hangman!")

#Main game loop
while True:
    display_word = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

#Prin the worf
    print("\nWord to guess:", display_word)


#Checks if the user has display word is equal to the chosen word
    if "_" not in display_word:
        print("\nCongratulations! You've guessed the word:", chosen_word)
        break

#User input
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

#Print the message
print("\nThanks for playing Hangman! Goodbye.")
