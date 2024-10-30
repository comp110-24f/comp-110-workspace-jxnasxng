__author__ = "730771663"


def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:
        return -1
    index: int = 0
    max: int = input[0]
    while index < len(input):
        if input[index] > max:
            max = input[index]
        index += 1
    index: int = 0
    while index < len(input):
        if input[index] == max:
            input.pop(index)
        else:
            index += 1
    return max
