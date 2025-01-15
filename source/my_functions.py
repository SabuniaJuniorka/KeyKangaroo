import string
import random


def generate_password(length_of_password):
    try:
        # take the input from user_input

        length_of_password = input("Enter the length of password: ")

        # get all characters needed to create secure password

        ascii_lowercase = list(string.ascii_lowercase)
        ascii_uppercase = list(string.ascii_uppercase)
        digits = list(string.digits)
        special_chars = list(string.punctuation)

        # delete characters that some site don't approve
        special_chars.remove("`")
        special_chars.remove("|")

        length_of_password = int(length_of_password)

        # check the length of the input and inform the user if the password is too short to be secure
        if length_of_password < 12:
            print("password is too short")
        elif length_of_password > 32:
            print("password is too long")
        else:

            # shuffle lists of characters

            random.shuffle(ascii_lowercase)
            random.shuffle(ascii_uppercase)
            random.shuffle(digits)
            random.shuffle(special_chars)

            # part the length of password in 2
            password_part_1 = round(length_of_password * 0.3)
            password_part_2 = round(length_of_password * 0.2)

            generated_signs = []

            # append the number of signs to the list of signs

            for sign in range(password_part_1):
                generated_signs.append(ascii_lowercase[sign])
                generated_signs.append(ascii_uppercase[sign])

            for sign in range(password_part_2):
                generated_signs.append(digits[sign])
                generated_signs.append(special_chars[sign])

            # shuffle generated signs once again

            random.shuffle(generated_signs)

            # make a password from random signs by joining them

            password = "".join(generated_signs)

            # display password

            print(f"Your password: {password}")

    except Exception as error:
        print(f"Error: {error}")
