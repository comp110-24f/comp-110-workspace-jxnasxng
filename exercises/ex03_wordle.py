__author__ = "730771663"


def input_guess(secret_word_len: int) -> str:
    # Takes word guess, and checks if the length is correct.
    word_input: str = input(f"Enter a {secret_word_len} character word: ")
    if len(word_input) == secret_word_len:
        print(word_input)
    else:
        # If length is not correct, prompts another guess from user.
        while len(word_input) != secret_word_len:
            print(f"That wasn't {secret_word_len} chars!")
            word_input = input("Try again: ")
        if len(word_input) == secret_word_len:
            return word_input
    return word_input


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Test each index of the word for a character match."""
    assert len(char_guess) == 1
    index: int = 0
    match: int = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            index += 1
            match += 1
        else:
            index += 1
    if match > 0:
        return True
    else:
        return False


def emojified(user_guess: str, secret_word: str) -> str:
    """Visualizes the accuracy of the guess."""
    assert len(user_guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    emojis: str = ""
    while index < len(secret_word):
        # Compiles the string of emojis to display.
        if user_guess[index] == secret_word[index]:
            emojis += GREEN_BOX
            index += 1
        elif (
            contains_char(secret_word=secret_word, char_guess=user_guess[index]) == True
        ):
            emojis += YELLOW_BOX
            index += 1
        else:
            emojis += WHITE_BOX
            index += 1
    return emojis


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    wins: int = 0
    while turns <= 6 and wins == 0:
        # Evaluates the user's guess when they have not won yet.
        print(f"=== Turn {turns}/6 ===")
        word_input: str = input_guess(secret_word_len=len(secret))
        print(emojified(user_guess=word_input, secret_word=secret))
        turns += 1
        if word_input == secret:
            # If the user guesses correctly, they will get out of the while loop.
            wins += 1
            turns -= 1
    if turns <= 6 and wins == 1:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
