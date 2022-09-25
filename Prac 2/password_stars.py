"""Password Check with Functions"""


def main():
    """Initialise the """
    password = get_password()
    while len(password) < 3:
        print("Invalid Password")
        password = get_password()
    display_asterisks(password)


def display_asterisks(password):
    """Display Asterisks"""
    for i in range(0, len(password)):
        print("*", end="")


def get_password():
    """Get password from user"""
    password = input("Password: ")
    return password


main()
