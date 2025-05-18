import re
import random
import string
import pyperclip

uppercase = re.compile(r'[A-Z]')
lowercase = re.compile(r'[a-z]')
digit = re.compile(r'\d')


def create_password():
    x = True
    strong_password = ""

    while x == True:
        n = random.randint(8,12)
        while len(strong_password)<n:
            new_char = random.choice(string.ascii_letters + string.digits)
            strong_password += new_char

        if uppercase.search(strong_password) != None \
           and lowercase.search(strong_password) != None \
           and digit.search(strong_password) != None:
            x = False
        else:
            strong_password = ""
            continue

    print(strong_password)
    pyperclip.copy(strong_password)
    press_enter = input("""\nPress any key to generate another one...\nPress 'q' to exit.""")
    if press_enter == "q":
        quit()
    else:
        create_password()

create_password()
