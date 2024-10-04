__author__ = "730771663"


def concat(str1: str, str2: str) -> str:
    return str1 + str2


word1: str = "happy"
word2: str = "tuesday"

print(concat(str1=word1, str2=word2))


def main() -> None:
    concat(str1=word1, str2=word2)


if __name__ == "__main__":
    main()
