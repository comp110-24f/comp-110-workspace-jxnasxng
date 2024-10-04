"""Mutating functions."""

___author___ = "730771663"


def manual_append(list: list[int], integer: int) -> None:
    list.append(integer)


def double(list: list[int]) -> None:
    index: int = 0
    while index < len(list):
        list[index] = 2 * list[index]
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list=list_2)
print(list_1)
print(list_2)
