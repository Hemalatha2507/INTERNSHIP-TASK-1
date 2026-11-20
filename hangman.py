import random

WORDS = ["python", "internship", "network", "security", "variable"]
MAX_WRONG = 6


def display_word(word, guessed):
    return " ".join(letter if letter in guessed else "_" for letter in word)


def play():
    word = random.choice(WORDS)
    guessed = []
    wrong = 0

    print("=== HANGMAN ===")
    print(f"Word {len(word)} letters . You have {MAX_WRONG} wrong guesses.\n")

    while wrong < MAX_WRONG:
        print(display_word(word, guessed))
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")
        print(f"Guessed so far: {' '.join(guessed) if guessed else '-'}")

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter only.\n")
            continue

        if guess in guessed:
            print("Already guess pannita! Try another.\n")
            continue

        guessed.append(guess)

        if guess in word:
            print("Correct!\n")
        else:
            wrong += 1
            print("Wrong!\n")

        if all(letter in guessed for letter in word):
            print(display_word(word, guessed))
            print(f"You won! Word: {word}")
            return

    print(f"Game over! The word was: {word}")


def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Bye! Thanks for playing.")
            break
        print()


if __name__ == "__main__":
    main()
