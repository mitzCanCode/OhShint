import random
import string

def generate_passwords(first_name, last_name, year):
    # Convert all inputs to lowercase for consistency
    first_name = first_name.lower()
    last_name = last_name.lower()

    # Create a list to store the potential passwords
    passwords = []

    # Existing combinations
    passwords.append(first_name + last_name + str(year))
    passwords.append(last_name + first_name + str(year))
    passwords.append(first_name + "." + last_name + str(year))
    passwords.append(last_name + "." + first_name + str(year))
    passwords.append(first_name + "_" + last_name + str(year))
    passwords.append(last_name + "_" + first_name + str(year))
    passwords.append(first_name[0] + last_name + str(year))
    passwords.append(first_name + last_name[0] + str(year))
    passwords.append(first_name[0] + "." + last_name + str(year))
    passwords.append(first_name + "." + last_name[0] + str(year))
    passwords.append(first_name[0] + "_" + last_name + str(year))
    passwords.append(first_name + "_" + last_name[0] + str(year))
    passwords.append(first_name[:2] + last_name + str(year))
    passwords.append(first_name + last_name[:2] + str(year))

    # Adding special characters and more complexity
    special_chars = "!@#$%^&*"
    
    for char in special_chars:
        passwords.append(first_name + last_name + str(year) + char)
        passwords.append(first_name + last_name + char + str(year))
        passwords.append(first_name + char + last_name + str(year))
        passwords.append(char + first_name + last_name + str(year))
        passwords.append(first_name + str(year) + last_name + char)
        passwords.append(first_name + str(year) + char + last_name)
        passwords.append(char + first_name + str(year) + last_name)
        passwords.append(first_name + last_name + char + str(year)[-2:])
        passwords.append(first_name[:2] + char + last_name + str(year)[-2:])
        passwords.append(first_name + last_name[:2] + str(year) + char)

    # Adding numeric and mixed case variations
    for num in range(10):
        passwords.append(first_name + last_name + str(year) + str(num))
        passwords.append(first_name + str(num) + last_name + str(year))
        passwords.append(str(num) + first_name + last_name + str(year))
        passwords.append(first_name.capitalize() + last_name.capitalize() + str(year))
        passwords.append(first_name.capitalize() + last_name + str(year))
        passwords.append(first_name + last_name.capitalize() + str(year))
        passwords.append(first_name.capitalize() + last_name + str(year) + str(num))
        passwords.append(first_name + last_name.capitalize() + str(year) + str(num))
    
    # Adding randomized characters
    for i in range(10):
        random_char = random.choice(string.ascii_letters + string.digits + special_chars)
        passwords.append(first_name + last_name + str(year) + random_char)
        passwords.append(first_name + random_char + last_name + str(year))
        passwords.append(random_char + first_name + last_name + str(year))
        passwords.append(first_name[:2] + last_name + str(year) + random_char)
        passwords.append(first_name + last_name[:2] + str(year) + random_char)

    

    # Make a file of the list of potential passwords
    filename = str(first_name+last_name+"Passwords.txt")
    f = open(filename, "w")
    for password in passwords:
        f.write(password+"\n")

    f.close()

