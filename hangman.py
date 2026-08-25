
import random

words = ['python', 'java', 'kotlin', 'javascript']

correct_word = random.choice(words)
wrong_guesses = 0
guessed = []


hangman = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\ |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\ |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]
max_attempts = len(hangman) - 1   # = 5, since indices go 0 to 5


print("Welcome to Hangman!")
print("Hint: The word is a Programming Language.")

while wrong_guesses < max_attempts:

    display = ""
    for letter in correct_word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print(hangman[wrong_guesses])
    print("Word:", display)


    if "_" not in display:
        print("Congratulations! You won!")
        print("The word was:", correct_word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess in correct_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print(hangman[wrong_guesses])
    print("Game Over!")
    print("The word was:", correct_word)
