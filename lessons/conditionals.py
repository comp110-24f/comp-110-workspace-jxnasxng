"""Practicing my conditionals."""


def less_than_10(num: int) -> bool:
    """Tell us if num < 10."""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:  # check if this is true
        print("Small number!")  # "then" block
    else:
        print("Big number!")
    print("Have a nice day!")


less_than_10(num=7)


def wake_up(alarm: bool) -> str:
    """Return a message based on if alarm is going off."""
    if alarm is True:
        return """Wake up!"""
    else:
        return """Keep sleeping. You deserve it."""


print(wake_up(alarm=True))


def check_first_letter(word: str, letter: str) -> str:
    """Checks if letter is first character of word."""
    if word[0] == letter:
        return "Match!"
    else:
        return "No match!"


# print(check_first_letter(word="happy", letter="h"))
