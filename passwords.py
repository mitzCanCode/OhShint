import random
import string
import os

def generate_passwords(first_name: str = "", last_name: str = "", bday: str = "", pet: str = "", nickname: str = "", file_name: str = "", size: str = "medium") -> list:
    # Convert all inputs to lowercase for consistency
    first_name = first_name.lower()
    last_name = last_name.lower()
    pet = pet.lower()
    nickname = nickname.lower()
    
    # Extract birthday components
    day = bday[:2]
    month = bday[:2]
    b_year = bday[4:]
    short_year = b_year[-2:]

    # Create a list to store the potential passwords
    passwords = []

    # Base combinations using first_name, last_name, pet, and nickname
    base_words = [first_name, last_name, pet, nickname]

    def add_passwords(word1, word2, year):
        """Helper function to generate password combinations"""
        if word1 and word2 and word1 != word2:
            # Full and short year combinations
            combinations = [
                word1 + word2 + year,
                word2 + word1 + year,
                word1 + "." + word2 + year,
                word2 + "." + word1 + year,
                word1 + "_" + word2 + year,
                word2 + "_" + word1 + year,
                word1[0] + word2 + year,
                word1 + word2[0] + year,
                word1[0] + "." + word2 + year,
                word1 + "." + word2[0] + year,
                word1[0] + "_" + word2 + year,
                word1 + "_" + word2[0] + year,
                word1[:2] + word2 + year,
                word1 + word2[:2] + year
            ]
            passwords.extend(combinations)

    # Generate base passwords with full and short years
    for word1 in base_words:
        for word2 in base_words:
            add_passwords(word1, word2, b_year)
            add_passwords(word1, word2, short_year)

    # Determine the number of passwords based on the desired size
    size_map = {
        "small": 500,
        "medium": 1500,
        "large": len(passwords)
    }
    
    target_password_count = size_map.get(size, 1500)
    
    # Adding special characters and more complexity
    special_chars = "!@#$%^&*"
    if size == "large":
        for char in special_chars:
            for base in passwords[:]:
                passwords.append(base + char)
                passwords.append(char + base)
                passwords.append(base[:len(base)//2] + char + base[len(base)//2:])
    
        # Adding numeric and mixed case variations
        for num in range(10):
            for base in passwords[:]:
                passwords.append(base + str(num))
                passwords.append(str(num) + base)
                passwords.append(base[:len(base)//2] + str(num) + base[len(base)//2:])
                passwords.append(base.capitalize() + str(num))
                passwords.append(str(num) + base.capitalize())
                passwords.append(base.capitalize())

        # Adding randomized characters
        for _ in range(10):
            random_char = random.choice(string.ascii_letters + string.digits + special_chars)
            for base in passwords[:]:
                passwords.append(base + random_char)
                passwords.append(random_char + base)
                passwords.append(base[:len(base)//2] + random_char + base[len(base)//2:])

    if size != "large":
        while len(passwords) < target_password_count:
            # Adding special characters
            for char in special_chars:
                for base in passwords[:]:
                    if len(passwords) < target_password_count:
                        passwords.append(base + char)
                        passwords.append(char + base)
                        passwords.append(base[:len(base)//2] + char + base[len(base)//2:])
            
            # Adding numeric and mixed case variations
            for num in range(10):
                for base in passwords[:]:
                    if len(passwords) < target_password_count:
                        passwords.append(base + str(num))
                        passwords.append(str(num) + base)
                        passwords.append(base[:len(base)//2] + str(num) + base[len(base)//2:])
                        passwords.append(base.capitalize() + str(num))
                        passwords.append(str(num) + base.capitalize())
                        passwords.append(base.capitalize())

            # Adding randomized characters
            for _ in range(10):
                random_char = random.choice(string.ascii_letters + string.digits + special_chars)
                for base in passwords[:]:
                    if len(passwords) < target_password_count:
                        passwords.append(base + random_char)
                        passwords.append(random_char + base)
                        passwords.append(base[:len(base)//2] + random_char + base[len(base)//2:])

            # Adding substitutions
            substitutions = {'o': '0', 'a': '@', 's': '$'}
            for base in passwords[:]:
                for orig, subs in substitutions.items():
                    if orig in base:
                        substituted = base.replace(orig, subs)
                        if len(passwords) < target_password_count:
                            passwords.append(substituted)

        passwords = passwords[:target_password_count]

    # Apply substitutions to all passwords
    substitutions = {'o': '0', 'a': '@', 's': '$'}
    substituted_passwords = []
    for base in passwords:
        for orig, subs in substitutions.items():
            if orig in base:
                substituted_passwords.append(base.replace(orig, subs))
    passwords.extend(substituted_passwords)

    # Ensure the passwords list is truncated to the target size if necessary
    passwords = passwords[:target_password_count]
    
    file_path = ""
    
    with open(file_name, "w") as f:
        for password in passwords:
            f.write(f"{password}\n")
        f.write(f"\nTotal passwords generated: {len(passwords)}")
        file_path = os.path.abspath(file_name)
        print("\033[94mFile was saved to:\033[0m", file_path)
            
    print(f"\033[94mTotal passwords generated:\033[0m {len(passwords)}")
    return passwords, file_path

if __name__ == "__main__":
    # Example usage:
    generate_passwords(first_name="Name", last_name="Surname", bday="12345678", pet="Kali", nickname="Nickname", file_name="name_lastname", size="medium")
