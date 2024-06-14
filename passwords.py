import random
import string

def generate_passwords(first_name, last_name, bday):
    # Convert all inputs to lowercase for consistency
    first_name = first_name.lower()
    last_name = last_name.lower()

    # Extract birthday components
    day = bday[:2]
    month = bday[2:4]
    b_year = bday[4:]
    short_year = b_year[-2:]

    # Create a list to store the potential passwords
    passwords = []

    # Existing combinations with full year
    base_passwords = [
        first_name + last_name + b_year,
        last_name + first_name + b_year,
        first_name + "." + last_name + b_year,
        last_name + "." + first_name + b_year,
        first_name + "_" + last_name + b_year,
        last_name + "_" + first_name + b_year,
        first_name[0] + last_name + b_year,
        first_name + last_name[0] + b_year,
        first_name[0] + "." + last_name + b_year,
        first_name + "." + last_name[0] + b_year,
        first_name[0] + "_" + last_name + b_year,
        first_name + "_" + last_name[0] + b_year,
        first_name[:2] + last_name + b_year,
        first_name + last_name[:2] + b_year
    ]
    
    # Existing combinations with short year
    base_passwords += [
        first_name + last_name + short_year,
        last_name + first_name + short_year,
        first_name + "." + last_name + short_year,
        last_name + "." + first_name + short_year,
        first_name + "_" + last_name + short_year,
        last_name + "_" + first_name + short_year,
        first_name[0] + last_name + short_year,
        first_name + last_name[0] + short_year,
        first_name[0] + "." + last_name + short_year,
        first_name + "." + last_name[0] + short_year,
        first_name[0] + "_" + last_name + short_year,
        first_name + "_" + last_name[0] + short_year,
        first_name[:2] + last_name + short_year,
        first_name + last_name[:2] + short_year
    ]
    
    passwords.extend(base_passwords)

    # Adding special characters and more complexity
    special_chars = "!@#$%^&*"
    for char in special_chars:
        for base in base_passwords:
            passwords.append(base + char)
            passwords.append(char + base)
            passwords.append(base[:len(base)//2] + char + base[len(base)//2:])
    
    # Adding numeric and mixed case variations
    for num in range(10):
        for base in base_passwords:
            passwords.append(base + str(num))
            passwords.append(str(num) + base)
            passwords.append(base[:len(base)//2] + str(num) + base[len(base)//2:])
            passwords.append(base.capitalize() + str(num))
            passwords.append(str(num) + base.capitalize())
            passwords.append(base.capitalize())

    # Adding randomized characters
    for _ in range(10):
        random_char = random.choice(string.ascii_letters + string.digits + special_chars)
        for base in base_passwords:
            passwords.append(base + random_char)
            passwords.append(random_char + base)
            passwords.append(base[:len(base)//2] + random_char + base[len(base)//2:])

    # Make a file of the list of potential passwords
    filename = f"{first_name}{last_name}Passwords.txt"
    with open(filename, "w") as f:
        for password in passwords:
            f.write(password + "\n")
