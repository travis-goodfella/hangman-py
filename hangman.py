import random

def get_random_word(word_list):
    """Select a random word from the given list of words."""
    return random.choice(word_list)

def display_current_state(word, guessed_letters):
    """Display the current state of the guessed word."""
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(display_word)

def display_hangman(incorrect_guesses):
    """Display the current stage of the hangman."""
    stages = [
        """
           -----
           |   |
               |
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
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    print(stages[incorrect_guesses])

def hangman():
    words = ["python", "algorithm", "snowden", "programming", "computer", "ransomware", "encryption", "database", "cyber", "developer", "malware", "phishing", "firewall"]
    word_to_guess = get_random_word(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while incorrect_guesses < max_incorrect_guesses:
        display_hangman(incorrect_guesses)
        display_current_state(word_to_guess, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            print(f"Good guess! {guess} is in the word.")
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(f"Wrong guess! {guess} is not in the word. You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"Congratulations! The word was '{word_to_guess}' good job!")
            return True

    display_hangman(incorrect_guesses)
    print(f"Game over! The word was '{word_to_guess}'.")
    return False

def main():
    while True:
        if hangman():
            play_again = input("GG! Play again? Enter y to play again or press enter to exit: ")
        else:
            play_again = input("Sorry, you lost. Play again? Enter y to play again or press enter to exit: ")
        if play_again != "y":
            break

if __name__ == "__main__":
    main()
