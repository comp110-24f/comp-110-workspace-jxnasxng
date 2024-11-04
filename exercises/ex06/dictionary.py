__author__ = "730771663"


def invert(input: dict[str, str]) -> dict[str, str]:
    # Function to make the keys become the values, and vice versa.
    inverted_dict: dict[str, str] = {}
    for key in input:
        if input[key] in inverted_dict:
            raise KeyError("Duplicate key.")
        inverted_dict[input[key]] = key
    return inverted_dict


def favorite_color(input: dict[str, str]) -> str:
    # Returns the most popular color.
    popular_color: str = ""
    colors_count: dict[str, int] = {}
    for key in input:
        if input[key] not in colors_count:
            colors_count[input[key]] = 1
        else:
            colors_count[input[key]] += 1
        if popular_color == "":
            popular_color = input[key]
        if colors_count[input[key]] > colors_count[popular_color]:
            popular_color = input[key]
    return popular_color


def count(input: list[str]) -> dict[str, int]:
    # Retrusn the number of times each item appears.
    nums: dict[str, int] = {}
    for x in range(len(input)):
        if input[x] in nums:
            nums[input[x]] += 1
        else:
            nums[input[x]] = 1
    return nums


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    # Returns a dictionary of letters, and list of words that
    # begin with that letter.
    pairs: dict[str, list[str]] = {}
    for x in range(len(words)):
        if words[x][0].lower() in pairs:
            pairs[words[x][0].lower()] = pairs[words[x][0].lower()] + [words[x]]
        else:
            pairs[words[x][0].lower()] = [words[x]]
    return pairs


def update_attendance(
    attendance_dict: dict[str, list[str]], day: str, student: str
) -> None:
    # Mutates the input with new attendance info.
    if day in attendance_dict:
        if student not in attendance_dict[day]:
            attendance_dict[day].append(student)
    else:
        attendance_dict[day] = [student]
