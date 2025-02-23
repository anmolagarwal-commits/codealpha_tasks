import random

def hangman_game():
    words = ['python', 'java', 'kotlin', 'codealpha']
    word = random.choice(words)
    guessed = set()
    turns = 5

    print("The word has", len(word), "letters.")

    while turns > 0:
        display_word = ''
        for letter in word:
            if letter in guessed:
                display_word += letter
            else:
                display_word += '_'
        print(display_word)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please input only one letter.")
            continue

        if not guess.isalpha():
            print("Please input a valid letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess not in word:
            turns -= 1
            print(f"Wrong guess! You have {turns} turns left.")
            if turns == 0:
                print(f"You lose. The word was: {word}")
                return

        all_guessed = True
        for letter in word:
            if letter not in guessed:
                all_guessed = False
                break

        if all_guessed:
            print(f"You win! The word was: {word}")
            return

hangman_game()
