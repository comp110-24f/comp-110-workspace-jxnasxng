__author__ = "730771663"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max() -> int:
    numbers: list[int] = [1, 2, 3, 4, 4]
    assert find_and_remove_max(numbers) == 4


def test_mutated_find_and_remove_max() -> None:
    numbers: list[int] = [1, 2, 3, 4, 4]
    find_and_remove_max(numbers)
    assert numbers == [1, 2, 3]


def test_edge_find_and_remove_max() -> int:
    numbers: list[int] = []
    assert find_and_remove_max(numbers) == -1
