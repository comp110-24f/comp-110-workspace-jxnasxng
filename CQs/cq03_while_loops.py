__author__ = "730771663"


# Function returns the amount of times a certain character appears in the str.
def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    # While loop to go over every character in "phrase."
    while index < len(phrase):
        # Checks to see if the current character is equal to search_char.
        # If so, then the count increases.
        if phrase[index] == search_char:
            count = count + 1
            index = index + 1
        else:
            index = index + 1
    return count
