__author__ = "730771663"


def all(list: list[int], num: int) -> bool:
    index: int = 0
    matches: int = 0
    if len(list) == 0:
        return False
    while index < len(list):
        if list[index] == num:
            matches += 1
            index += 1
        else:
            index += 1
    if matches == len(list):
        return True
    else:
        return False


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 1
    max_int: int = input[0]
    while index < len(input):
        if input[index] > max_int:
            max_int = input[index]
            index += 1
        else:
            index += 1
    return max_int


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    index: int = 0
    matches: int = 0
    while index < (len(list_1) or len(list_2)):
        if list_1[index] == list_2[index]:
            matches += 1
            index += 1
        else:
            index += 1
    if matches == (len(list_1) or len(list_2)):
        return True
    else:
        return False


def extend(a: list[int], b: list[int]) -> None:
    index: int = 0
    while index < len(b):
        a.append(b[index])
        index += 1
