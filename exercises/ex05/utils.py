__author__ = "730771663"


# Takes all the even ints in the inputted list
# And adds them to, and returns, a new list.
def only_evens(input: list[int]) -> list[int]:
    even_list: list[int] = []
    for x in input:
        if x % 2 == 0:
            even_list.append(x)
    return even_list


def sub(input: list[int], start_index: int, end_index: int) -> list[int]:
    sub_list: list[int] = []
    if start_index < 0:
        start_index = 0
    if end_index > len(input):
        end_index = len(input)
    if len(input) == 0 or start_index >= len(input) or end_index <= 0:
        return []
    sub_list: list[int] = []
    for idx in range(start_index, end_index):
        sub_list.append(input[idx])
    return sub_list


def add_at_index(input: list[int], num: int, index: int) -> None:
    if index < 0 or index > len(input):
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)
    first = num
    for x in range(index, len(input)):
        right: int = input[x]
        input[x] = first
        first = right
