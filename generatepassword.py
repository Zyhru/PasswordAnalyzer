import random
import array

# Generating password based on user inputs length


# Minimum length of a password will be 8 
# Maximum length of a password will be 16
# The password will select a random character from all uppercase,lowercase,special, and number characters.

# 1. Ask user to input desired length for their password
# 2. Loop from 8 until to user input
# 3. Select a random character 
# 4. Concatenate to string
# 5. Return string


def random_character(a):

    character_list = list(a)
    # random.randrange(len(character_list))
    random_char = character_list[random.randrange(len(character_list))]

    return random_char


def generate_password():

    password_length = int(input("Enter length of password: "))

    password = ""

    alphabet_lc = "abcdefghijklmnopqrstuvwxyz"
    alphabet_uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_characters = "`!@#$%^&*()-_+=[]|;:<>,./?"
        
    for x in range(password_length):

     random_number = random.randrange(1,5)

     if random_number == 1:
         password += random_character(alphabet_lc) 
     elif random_number == 2:
         password += random_character(alphabet_uc)
     elif random_number == 3:
         password += random_character(numbers)
     elif random_number == 4:
         password += random_character(special_characters)


    password_list = array.array('u', password)
    

    test = ""
    for y in password_list:
        test += y
    
    return test


print(generate_password())