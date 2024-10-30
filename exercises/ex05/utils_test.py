__author__ = "730771663"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


# only_evens tests
def test_only_evens_return() -> None:
    input: list[int] = [1, 2, 3, 4]
    assert only_evens(input)


def test_only_evens_mutation() -> None:
    mutated_list: list[int] = [2, 4]
    assert only_evens([1, 2, 3, 4]) == [2, 4]
    assert mutated_list == [2, 4]


def test_only_evens_edge() -> None:
    input: list[int] = []
    assert only_evens(input) == []


# Test sub


def test_sub_return() -> None:
    # Returns list of ints at index 0 and 1
    input: list[int] = [3, 6, 9, 12]
    assert sub(input, 0, 2)


def test_sub_not_mutated() -> None:
    result: list[int] = [5, 6, 7, 8]
    sub(result, 0, 1)
    assert result == [5, 6, 7, 8]


def test_sub_edge() -> None:
    input: list[int] = [2, 4, 6, 8]
    assert sub(input, -10, 10) == [2, 4, 6, 8]


# Test add_at_index


def test_add_at_index_list() -> None:
    input: list[int] = [10, 20, 30, 40]
    add_at_index(input, 50, 4)
    assert input == [10, 20, 30, 40, 50]


def test_add_at_index_return() -> None:
    input: list[int] = [3, 2, 1]
    assert add_at_index(input, 0, 0) == None


def test_add_at_index_raises_indexerror():
    input: list[int] = []
    with pytest.raises(IndexError):
        add_at_index(input, 1, 2)
