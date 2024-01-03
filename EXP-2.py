import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "algorithm", "developer", "gaming", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed_letters = []
    attempts_left = 6

    while attempts_left > 0:
        print("\nAttempts left:", attempts_left)
        current_display = display_word(secret_word, guessed_letters)
        print("Current word:", current_display)

        guess = input("Enter a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
            elif guess in secret_word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess. Try again.")
                guessed_letters.append(guess)
                attempts_left -= 1
        else:
            print("Invalid input. Please enter a single letter.")

        if set(secret_word) <= set(guessed_letters):
            print("\nCongratulations! You've guessed the word:", secret_word)
            break

    if attempts_left == 0:
        print("\nSorry, you've run out of attempts. The correct word was:", secret_word)

if __name__ == "__main__":
    hangman()
