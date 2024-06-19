import os

def generate_usernames(first_name: str = "", last_name: str = "", bday: str = "", file_name: str = "", prnt: bool = True) -> list:
    # Convert all inputs to lowercase for consistency
    first_name = first_name.lower()
    last_name = last_name.lower()
    
    # Create a list to store the potential usernames
    usernames = []

    # Birthday components
    day = bday[:2] if bday else ""
    month = bday[2:4] if bday else ""
    b_year = bday[4:] if bday else ""

    if not bday:
        # Add different combinations of first name and last name
        if first_name:
            usernames.append(first_name)
        if last_name:
            usernames.append(last_name)
        if first_name and last_name:
            usernames.extend([
                first_name + last_name, last_name + first_name,
                first_name + "." + last_name, last_name + "." + first_name,
                first_name + "_" + last_name, last_name + "_" + first_name,
                first_name[0] + last_name, first_name + last_name[0],
                first_name[0] + "." + last_name, first_name + "." + last_name[0],
                first_name[0] + "_" + last_name, first_name + "_" + last_name[0],
                last_name + last_name[-1], first_name + first_name[-1],
                first_name + last_name + last_name[-1], first_name[0] + last_name,
                first_name + first_name[-1] + last_name[0], first_name[0] + "." + last_name + last_name[-1],
                first_name + first_name[-1] + "." + last_name[0], first_name[0] + "_" + last_name,
                first_name + "_" + last_name[0], first_name[:2] + last_name,
                first_name[:2] + last_name, first_name + last_name + "123",
                first_name + "." + last_name + "123", first_name + "_" + last_name + "123",
                first_name[0] + last_name + "123", first_name + last_name[0] + "123",
                first_name[:2] + last_name + "123", first_name + last_name[:2] + "123"
            ])

    else:
        if first_name:
            usernames.append(first_name)
        if last_name:
            usernames.append(last_name)
        if first_name and last_name:
            usernames.extend([
                first_name + last_name, last_name + first_name,
                first_name + "." + last_name, last_name + "." + first_name,
                first_name + "_" + last_name, last_name + "_" + first_name,
                first_name[0] + last_name, first_name + last_name[0],
                first_name[0] + "." + last_name, first_name + "." + last_name[0],
                first_name[0] + "_" + last_name, first_name + "_" + last_name[0],
                last_name + last_name[-1], first_name + first_name[-1],
                first_name + last_name + last_name[-1], first_name[0] + last_name,
                first_name + first_name[-1] + last_name[0], first_name[0] + "." + last_name + last_name[-1],
                first_name + first_name[-1] + "." + last_name[0], first_name[0] + "_" + last_name,
                first_name + "_" + last_name[0], first_name[:2] + last_name,
                first_name[:2] + last_name, first_name + last_name + day,
                first_name + last_name + month, first_name + last_name + b_year,
                first_name + "." + last_name + day, first_name + "." + last_name + month,
                first_name + "." + last_name + b_year, first_name + "_" + last_name + day,
                first_name + "_" + last_name + month, first_name + "_" + last_name + b_year,
                first_name[0] + last_name + day, first_name[0] + last_name + month,
                first_name[0] + last_name + b_year, first_name + last_name[0] + day,
                first_name + last_name[0] + month, first_name + last_name[0] + b_year,
                first_name[:2] + last_name + day, first_name[:2] + last_name + month,
                first_name[:2] + last_name + b_year, first_name + last_name[:2] + day,
                first_name + last_name[:2] + month, first_name + last_name[:2] + b_year,
                first_name + last_name + str(b_year)[-2:], first_name + "." + last_name + str(b_year)[-2:],
                first_name + "_" + last_name + str(b_year)[-2:], first_name[0] + last_name + str(b_year)[-2:],
                first_name + last_name[0] + str(b_year)[-2:], first_name[:2] + last_name + str(b_year)[-2:],
                first_name + last_name[:2] + str(b_year)[-2:], first_name[:2] + last_name + "_" + str(b_year)[-2:],
                first_name + "_" + last_name[:2] + str(b_year)[-2:], first_name[0] + last_name[:2] + str(b_year)[-2:],
                first_name[:2] + last_name[0] + str(b_year)[-2:], first_name + last_name + "123",
                first_name + "." + last_name + "123", first_name + "_" + last_name + "123",
                first_name[0] + last_name + "123", first_name + last_name[0] + "123",
                first_name[:2] + last_name + "123", first_name + last_name[:2] + "123"
            ])

        # If only first_name or last_name is provided along with birthday
        if first_name and not last_name:
            usernames.extend([
                first_name + day, first_name + month, first_name + b_year,
                first_name + "." + day, first_name + "." + month, first_name + "." + b_year,
                first_name + "_" + day, first_name + "_" + month, first_name + "_" + b_year,
                first_name[0] + day, first_name[0] + month, first_name[0] + b_year,
                first_name[:2] + day, first_name[:2] + month, first_name[:2] + b_year,
                first_name + str(b_year)[-2:], first_name + "." + str(b_year)[-2:], first_name + "_" + str(b_year)[-2:],
                first_name[0] + str(b_year)[-2:], first_name[:2] + str(b_year)[-2:], first_name + "123",
                first_name + "." + "123", first_name + "_" + "123", first_name[0] + "123",
                first_name[:2] + "123"
            ])

        if last_name and not first_name:
            usernames.extend([
                last_name + day, last_name + month, last_name + b_year,
                last_name + "." + day, last_name + "." + month, last_name + "." + b_year,
                last_name + "_" + day, last_name + "_" + month, last_name + "_" + b_year,
                last_name[0] + day, last_name[0] + month, last_name[0] + b_year,
                last_name[:2] + day, last_name[:2] + month, last_name[:2] + b_year,
                last_name + str(b_year)[-2:], last_name + "." + str(b_year)[-2:], last_name + "_" + str(b_year)[-2:],
                last_name[0] + str(b_year)[-2:], last_name[:2] + str(b_year)[-2:], last_name + "123",
                last_name + "." + "123", last_name + "_" + "123", last_name[0] + "123",
                last_name[:2] + "123"
            ])

    with open(file_name, "w") as f:
        for i in range(len(usernames)):
            if prnt:
                print(f"\033[94m{i}. {usernames[i]}\033[0m")
            f.write(usernames[i] + "\n")
        f.write(f"\nTotal usernames generated: {len(usernames)}")
        file_path = os.path.abspath(file_name)
        print(f"\033[94mFile was saved to: {file_path}\033[0m")
        print(f"\033[94mTotal usernames generated: {len(usernames)}\033[0m")
            
    return usernames, file_path

if __name__ == "__main__":
    generate_usernames(first_name="name", last_name="surname", bday="12345678", file_name="name_lastname_usernames.txt", prnt=True)
