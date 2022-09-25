"""Menu"""
MENU = """R - Result
S - Stars
Q - Quit"""


def main():
    print(MENU)
    choice = input("Choice >>> ").upper()
    while choice != "Q":
        if choice == "R":
            score = get_valid_score()
            outcome = parameter(score)
            print(outcome)
            print(MENU)
            choice = input("Choice >>> ").upper()
        elif choice == "S":
            score = get_valid_score()
            display_asterisks(score)
            print("""\nR - Result
S - Stars
Q - Quit"""
                  )
            choice = input("Choice >>> ").upper()
    print(f"Finished!")


def get_valid_score():
    """Determine if users score is valid"""
    score = int(input("Enter score: "))
    if 0 > score > 100:
        print("Invalid Score")
    else:
        return score


def parameter(score):
    """Determine users score category"""
    if 0 < score > 100:
        return "Invalid score"
    elif score >= 50:
        return "Passable"
    elif score >= 90:
        return "Excellent"
    else:
        return "Bad"


def display_asterisks(score):
    """Display Asterisks"""
    for i in range(0, score):
        print("*", end="")


main()
