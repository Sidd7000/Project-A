import random

def choose_random_word():
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    secret_word = choose_random_word()
    guessed_letters = []
    attempts = 6  # Number of attempts allowed

    print("Welcome to Hangman!")

    while attempts > 0:
        print(display_word(secret_word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!")
            if display_word(secret_word, guessed_letters) == secret_word:
                print("Congratulations, you've won! The word was:", secret_word)
                break
        else:
            print("Incorrect guess.")
            attempts -= 1
            print(f"You have {attempts} attempts left.")

    if attempts == 0:
        print("Sorry, you've run out of attempts. The word was:", secret_word)

if __name__ == "__main__":
    hangman()
