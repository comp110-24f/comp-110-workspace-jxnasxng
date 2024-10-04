"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730771663"


# Will take a word that the user inputted.
def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
    else:
        # If the word is not 5 letters long, then an error message
        # will show, and the program will exit.
        print("Error: Word must contain 5 characters.")
        exit()
        return word


# Will take a letter that the user inputs.
def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        # If the letter is not one character long, program will exit.
        print("Error: Character must be a single character.")
        exit()
        return letter


# Finds how many times the inputted letter is found
# in the inputted word.
def contains_char(word: str, letter: str) -> None:
    index: int = 0
    count: int = 0
    print("Searching for " + letter + " in " + word)
    while index < len(word):
        if word[index] == letter:
            print(letter + " found at index " + str(index))
            index = index + 1
            count = count + 1
        else:
            index = index + 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


# Pulls all the functions together when called.
def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
