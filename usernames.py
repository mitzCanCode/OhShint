def generate_usernames(first_name: str = "", last_name: str = "", bday: str = "", prnt = bool) -> list:
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
            usernames.append(first_name + last_name)
            usernames.append(last_name + first_name)
            usernames.append(first_name + "." + last_name)
            usernames.append(last_name + "." + first_name)
            usernames.append(first_name + "_" + last_name)
            usernames.append(last_name + "_" + first_name)

            usernames.append(first_name[0] + last_name)
            usernames.append(first_name + last_name[0])
            usernames.append(first_name[0] + "." + last_name)
            usernames.append(first_name + "." + last_name[0])
            usernames.append(first_name[0] + "_" + last_name)
            usernames.append(first_name + "_" + last_name[0])

            usernames.append(last_name + last_name[-1])
            usernames.append(first_name + first_name[-1])
            usernames.append(first_name + last_name + last_name[-1])
            usernames.append(first_name[0] + last_name)
            usernames.append(first_name + first_name[-1] + last_name[0])
            usernames.append(first_name[0] + "." + last_name + last_name[-1])
            usernames.append(first_name + first_name[-1] + "." + last_name[0])
            usernames.append(first_name[0] + "_" + last_name)
            usernames.append(first_name + "_" + last_name[0])
            usernames.append(first_name[:2] + last_name)
            usernames.append(first_name[:2] + last_name)

            usernames.append(first_name + last_name + "123")
            usernames.append(first_name + "." + last_name + "123")
            usernames.append(first_name + "_" + last_name + "123")
            usernames.append(first_name[0] + last_name + "123")
            usernames.append(first_name + last_name[0] + "123")
            usernames.append(first_name[:2] + last_name + "123")
            usernames.append(first_name + last_name[:2] + "123")

    else:
        if first_name:
            usernames.append(first_name)
        if last_name:
            usernames.append(last_name)
        if first_name and last_name:
            usernames.append(first_name + last_name)
            usernames.append(last_name + first_name)
            usernames.append(first_name + "." + last_name)
            usernames.append(last_name + "." + first_name)
            usernames.append(first_name + "_" + last_name)
            usernames.append(last_name + "_" + first_name)

            usernames.append(first_name[0] + last_name)
            usernames.append(first_name + last_name[0])
            usernames.append(first_name[0] + "." + last_name)
            usernames.append(first_name + "." + last_name[0])
            usernames.append(first_name[0] + "_" + last_name)
            usernames.append(first_name + "_" + last_name[0])

            usernames.append(last_name + last_name[-1])
            usernames.append(first_name + first_name[-1])
            usernames.append(first_name + last_name + last_name[-1])
            usernames.append(first_name[0] + last_name)
            usernames.append(first_name + first_name[-1] + last_name[0])
            usernames.append(first_name[0] + "." + last_name + last_name[-1])
            usernames.append(first_name + first_name[-1] + "." + last_name[0])
            usernames.append(first_name[0] + "_" + last_name)
            usernames.append(first_name + "_" + last_name[0])
            usernames.append(first_name[:2] + last_name)
            usernames.append(first_name[:2] + last_name)

            usernames.append(first_name + last_name + day)
            usernames.append(first_name + last_name + month)
            usernames.append(first_name + last_name + b_year)
            usernames.append(first_name + "." + last_name + day)
            usernames.append(first_name + "." + last_name + month)
            usernames.append(first_name + "." + last_name + b_year)
            usernames.append(first_name + "_" + last_name + day)
            usernames.append(first_name + "_" + last_name + month)
            usernames.append(first_name + "_" + last_name + b_year)

            usernames.append(first_name[0] + last_name + day)
            usernames.append(first_name[0] + last_name + month)
            usernames.append(first_name[0] + last_name + b_year)
            usernames.append(first_name + last_name[0] + day)
            usernames.append(first_name + last_name[0] + month)
            usernames.append(first_name + last_name[0] + b_year)

            usernames.append(first_name[:2] + last_name + day)
            usernames.append(first_name[:2] + last_name + month)
            usernames.append(first_name[:2] + last_name + b_year)
            usernames.append(first_name + last_name[:2] + day)
            usernames.append(first_name + last_name[:2] + month)
            usernames.append(first_name + last_name[:2] + b_year)

            usernames.append(first_name + last_name + str(b_year)[-2:])
            usernames.append(first_name + "." + last_name + str(b_year)[-2:])
            usernames.append(first_name + "_" + last_name + str(b_year)[-2:])
            usernames.append(first_name[0] + last_name + str(b_year)[-2:])
            usernames.append(first_name + last_name[0] + str(b_year)[-2:])
            usernames.append(first_name[:2] + last_name + str(b_year)[-2:])
            usernames.append(first_name + last_name[:2] + str(b_year)[-2:])
            usernames.append(first_name[:2] + last_name + "_" + str(b_year)[-2:])
            usernames.append(first_name + "_" + last_name[:2] + str(b_year)[-2:])
            usernames.append(first_name[0] + last_name[:2] + str(b_year)[-2:])
            usernames.append(first_name[:2] + last_name[0] + str(b_year)[-2:])

            usernames.append(first_name + last_name + "123")
            usernames.append(first_name + "." + last_name + "123")
            usernames.append(first_name + "_" + last_name + "123")
            usernames.append(first_name[0] + last_name + "123")
            usernames.append(first_name + last_name[0] + "123")
            usernames.append(first_name[:2] + last_name + "123")
            usernames.append(first_name + last_name[:2] + "123")

        # If only first_name or last_name is provided along with birthday
        if first_name and not last_name:
            usernames.append(first_name + day)
            usernames.append(first_name + month)
            usernames.append(first_name + b_year)
            usernames.append(first_name + "." + day)
            usernames.append(first_name + "." + month)
            usernames.append(first_name + "." + b_year)
            usernames.append(first_name + "_" + day)
            usernames.append(first_name + "_" + month)
            usernames.append(first_name + "_" + b_year)

            usernames.append(first_name[0] + day)
            usernames.append(first_name[0] + month)
            usernames.append(first_name[0] + b_year)

            usernames.append(first_name[:2] + day)
            usernames.append(first_name[:2] + month)
            usernames.append(first_name[:2] + b_year)

            usernames.append(first_name + str(b_year)[-2:])
            usernames.append(first_name + "." + str(b_year)[-2:])
            usernames.append(first_name + "_" + str(b_year)[-2:])
            usernames.append(first_name[0] + str(b_year)[-2:])
            usernames.append(first_name[:2] + str(b_year)[-2:])

            usernames.append(first_name + "123")
            usernames.append(first_name + "." + "123")
            usernames.append(first_name + "_" + "123")
            usernames.append(first_name[0] + "123")
            usernames.append(first_name[:2] + "123")

        if last_name and not first_name:
            usernames.append(last_name + day)
            usernames.append(last_name + month)
            usernames.append(last_name + b_year)
            usernames.append(last_name + "." + day)
            usernames.append(last_name + "." + month)
            usernames.append(last_name + "." + b_year)
            usernames.append(last_name + "_" + day)
            usernames.append(last_name + "_" + month)
            usernames.append(last_name + "_" + b_year)

            usernames.append(last_name[0] + day)
            usernames.append(last_name[0] + month)
            usernames.append(last_name[0] + b_year)

            usernames.append(last_name[:2] + day)
            usernames.append(last_name[:2] + month)
            usernames.append(last_name[:2] + b_year)

            usernames.append(last_name + str(b_year)[-2:])
            usernames.append(last_name + "." + str(b_year)[-2:])
            usernames.append(last_name + "_" + str(b_year)[-2:])
            usernames.append(last_name[0] + str(b_year)[-2:])
            usernames.append(last_name[:2] + str(b_year)[-2:])

            usernames.append(last_name + "123")
            usernames.append(last_name + "." + "123")
            usernames.append(last_name + "_" + "123")
            usernames.append(last_name[0] + "123")
            usernames.append(last_name[:2] + "123")

    # Make a file with the usernames list if both first_name and last_name are provided
    if first_name and last_name:
        filename = str(first_name + last_name + "Usernames.txt")
        with open(filename, "w") as f:
            for i in range(len(usernames)):
                if prnt:
                    print(str(i)+". "+ usernames[i])
                f.write(str(i)+". "+ usernames[i] + "\n")

    return usernames
