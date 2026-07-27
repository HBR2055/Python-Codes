# imporing modules
import string
import random

# characters to create pass
characters = list (string.ascii_letters + string.digits + '!@#$%^&*()"' )

def generate_random_pass():
    # lenght of pass from user
    length = int(input("Enter Pass Length: "))

    # shuffling the characters
    random.shuffle(characters)

    # picking random pass from list
    passcode = []
    for i in range(length):
        passcode.append(random.choice(characters))

    # shuffling the resultant pass
    random.shuffle(passcode)
    # converting the list to string
    # printing the list
    print("".join(passcode))
# invoking the function
generate_random_pass()
