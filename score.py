from random import randint


def main():
    score = float(input("Enter score: "))
    outcome = parameter(score)
    print(outcome)
    score = randint(0, 100)
    print(f"Random Score: {score}")
    outcome = parameter(score)
    print(outcome)


def parameter(score):
    if 0 < score > 100:
        return "Invalid score"
    elif score >= 50:
        return "Passable"
    elif score >= 90:
        return "Excellent"
    else:
        return "Bad"


main()
