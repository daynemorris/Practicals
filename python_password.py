password = input("Password: ")
while len(password) < 3:
    print("Invalid Password")
    password = input("Password: ")
for i in range(0, len(password) + 1):
    print("*", end="")
