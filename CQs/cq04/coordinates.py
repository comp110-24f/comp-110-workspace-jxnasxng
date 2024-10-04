__author__ = "730771663"


def get_coords(xs: str, ys: str) -> None:
    idx: int = 0
    while idx < len(xs):
        index: int = 0
        while index < len(ys):
            print(f"({xs[idx]},{ys[index]})")
            index += 1
        idx += 1
