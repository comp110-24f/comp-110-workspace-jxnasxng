"""Basic syntax of lists."""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

# Add items to list
my_numbers.append(1.5)
my_numbers.append(2.3)

# Create an already populated list.
game_points: list[int] = [102, 86, 94]

# Subscription Notation / Indexing
print(game_points[2])
last_game: int = game_points[2]
print(last_game)

# Modifying by Index
game_points[1] = 72
print(game_points)

# Removing an element
game_points.pop(1)
print(game_points)


# Write a function called display
# Input: list[int]
# Return value: none
# Loop over the input and print every value
# Try calling it on game_points
def display(list: list[int]) -> None:
    index: int = 0
    while index < len(list):
        print(list[index])
        index += 1


display(game_points)
print(my_numbers[10])
