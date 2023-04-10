import string
import random

characters = list(string.ascii_letters + string.digits + " !@#$%^&*()")


def generate_password():
    password_length = int(input("Length of the password : ? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)


option = input("Do you want to generate a password? (Yes/No): ")

if option == "Yes" or option == "YES" or option == "yes":
    print("Hurray generating the password for you !!!")
    generate_password()
elif option == "No" or option == "NO" or option == "no":
    print("Program ended, see you next time")
    quit()
else:
    print("Invalid input, please input (Yes,YES,yes) or (No,NO,no)")
    quit()