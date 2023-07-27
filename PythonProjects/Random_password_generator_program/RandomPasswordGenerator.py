# Ask user if they to generate a password or not
# If yes, ask for password length
# print the password
# If initial response is no, exit program


import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%|^:;")

def generate_password():
    password_length = int(input("How long would you like your password to be?"))
    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)



option = input("Do you want to generate a password (yes/no): ")

if option == "yes":
    generate_password()
elif option == "no":
    print("program Ended")
    quit()
else:
    print("Invalid input, please input Yes or NO")
    quit()

