def generate_usernames(first_name, last_name, bday):
    # Convert all inputs to lowercase for consistency
    first_name = first_name.lower()
    last_name = last_name.lower()
    
    # Create a list to store the potential usernames
    usernames = []


    # Birthday components
    day = bday[:2]
    month = bday[2:4]
    b_year = bday[4:]
    
    if bday == "":
        # Add different combinations of first name and last name
        usernames.append(first_name)
        usernames.append(last_name)
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
        usernames.append(first_name+ first_name[-1] + "." + last_name[0])
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
        usernames.append(first_name)
        usernames.append(last_name)
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
        usernames.append(first_name+ first_name[-1] + "." + last_name[0])
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



    # Make a file with the usernames list
    filename = str(first_name+last_name+"Usernames.txt")
    f = open(filename, "w")
    for name in usernames:
        f.write(name+"\n")

    f.close()

