"""Tea party."""

__author__ = "730771663"


# The inputted guest amount is used for all of these functions.
# The cost is calculated by using functions with a function.
def main_planner(guests: int) -> None:
    """Brings all of the functions together."""
    print("A Cozy Tea Party for " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests))))


def tea_bags(people: int) -> int:
    """Will return the number of tea bags needed."""
    return 2 * people


def treats(people: int) -> int:
    """Returns the number of treats needed."""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Returns the total cost of the tea party."""
    return (0.5 * tea_count) + (0.75 * treat_count)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
