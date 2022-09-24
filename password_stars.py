"""Password Check with Functions"""


def main():
    password = get_password()
    while len(password) < 3:
        print("Invalid Password")
        password = get_password()
    display_asterisks(password)


def display_asterisks(password):
    for i in range(0, len(password) + 1):
        print("*", end="")


def get_password():
    password = input("Password: ")
    return password


main()
