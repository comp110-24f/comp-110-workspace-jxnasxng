def remove_chars(msg: str, char: str) -> str:
    copy: str = ""
    index: int = 0
    while index < len(msg):
        if not (msg[index] == char):
            copy += msg[index]
        index += 1
    return copy


word: str = "yoyo"
print(remove_chars(msg=word, char="o"))
