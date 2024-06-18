from passwords import generate_passwords
from usernames import generate_usernames
# from image_metadata import metadata_extractor, clear_metadata
from lookup import search
import os
import sys

mtdata_help_message = """
mtdata - Metadata extraction and clearing tool

Usage:
  mtdata <file_path> [options] 

Options:
  -h                Show this help message
  -c                Clear metadata from the specified file
  -o                Overwrite the original images metadata if clearing its metadata instead of creating a new image
  -mn               Display MakerNote metadata (hidden by default)

Examples:
  mtdata image.jpg                  Extract metadata from image.jpg and display it
  mtdata image.jpg -mn              Extract metadata from image.jpg, including MakerNote data, and display it
  mtdata image.jpg -c               Clear metadata from image.jpg and save the result as modified_image.jpg
  mtdata image.jpg  -c -o 		    Clear metadata from image.jpg and save the result as new_image.jpg
"""

usr_help_message = """
Username finder - Generates potential usernames

Usage:
    usr [options]

Options:
    -h             Show this help message
    -n             Name that will be used to generate usernames
    -l             Lastname that will be used to generate usernames
    -b             Birthday that will be used to generate usernames (format: DDMMYYYY)
    -p             Print all the usernames
    -s             Save all the usernames on a txt file
    -fn            Set a custom file name

Examples:
    usr -n Name -l Surname -b 13052000 -p -s
    usr -l Surname -b 15031969
    usr -N Name -l Surname -p -s -fn fileName

"""
pass_help_message = """
Password finder - Generates potential passwords

Usage:
    pass [options]

Options:
    -h             Show this help message
    -n             Name that will be used to generate passwords
    -l             Lastname that will be used to generate passwords
    -b             Birthday that will be used to generate passwords (format: DDMMYYYY)
    -p             Print all the passwords
    -s             Save all the passwords in a txt file
    -fn            Set a custom file name

Examples:
    pass -n Name -l Surname -b 13052000 -p -s
    pass -l Surname -b 15031969
    pass -N Name -l Surname -p -s -fn fileName
"""

lookup_help_message = """
Lookup - Searches for user information based on a username

Usage:
    lookup <username> [options]

Options:
    -h             Show this help message
    -i <ID>        Use the username associated with the given ID from the generated usernames list

Examples:
    lookup username
    lookup -i 2

Notes:
    To use the -i option, you must first generate a list of usernames using the usr command.
    The command searches for information related to the specified username and displays the results.

"""

show_help_message = """
"""

try:
    while True:

            prompt = input("OhShint! > ")
            prompt = prompt.split()
            
            if prompt[0] == "exit":
                print("Quitting...")
                sys.exit()
            elif prompt[0] == "help":
                print("Help message here")
                continue
            elif prompt[0] == "usr":


                name, last_name, bday, prnt, save = None, None, None, False, False
                
                if "-h" in prompt:
                    print(usr_help_message)
                    continue

                if "-n" in prompt:
                    name = prompt[prompt.index("-n") + 1]

                if "-l" in prompt:
                    last_name = prompt[prompt.index("-l") + 1]
                
                if "-fn" in prompt:
                    file_name = prompt[prompt.index("-fn") + 1]

                if "-b" in prompt:
                    bday = prompt[prompt.index("-b") + 1]

                if "-p" in prompt:
                    prnt = True

                if "-s" in prompt:
                    save = True

                temp = generate_usernames(name, last_name, bday, file_name, prnt, save)

                usernames = {index: username for index, username in enumerate(temp)}


            elif prompt[0] == "pass":

                prnt = False
                save = False
                name, last_name, bday, file_name, prnt, save = None, None, None, False, False


                if "-h" in prompt:
                    print(pass_help_message)
                    continue

                if "-n" in prompt:
                    name = prompt[prompt.index("-n") + 1]

                if "-l" in prompt:
                    last_name = prompt[prompt.index("-l") + 1]
                
                if "-fn" in prompt:
                    file_name = prompt[prompt.index("-fn") + 1]

                if "-b" in prompt:
                    bday = prompt[prompt.index("-b") + 1]

                if "-p" in prompt:
                    prnt = True

                if "-s" in prompt:
                    save = True

                temp = generate_passwords(name, last_name, bday, file_name, prnt, save)

                passwords = {index: password for index, password in enumerate(temp)}
                
            
            elif prompt[0] == "show":
                if "-h" in prompt:
                    print(show_help_message)
                    continue
                if "usernames" in prompt:
                    if usernames:
                        for k, v in usernames.items():
                            print(f"{k}: {v}")
                        continue
                    else:
                        print("Please generate a username list first.")
                        continue
                elif "lookup" in prompt:
                    if lookup_results:
                        for k, v in lookup_results.items():
                            print(f"{k}: {v}")
                        continue
                    else:
                        print("Please complete a lookup first.")
                        continue
            
            elif prompt[0] == "lookup":
                if "-h" in prompt:
                    print(lookup_help_message)
                    continue
                
                if "-i" in prompt:
                    try:
                        id = prompt[prompt.index("-i") + 1]
                    except IndexError:
                        print("Please specify an ID")
                        continue
                    except Exception as e:
                        print(e)
                    if not usernames:
                        print("Generate a usernames list to start using IDs")
                        continue
                    
                    try: 
                        id = int(id)
                    except:
                        print("ID must be number")
                        continue
                    
                    try: 
                        username = usernames[id]
                        print(username)
                    except:
                        print("Please select an ID in the list of usernames generated")
                        continue
                    
                    try:
                        lookup_results = search(username)
                    except Exception as e:
                        print(f"Error: {e}")
                        continue
                else:
                    try:
                        username = prompt[1]
                    except IndexError:
                        print("Please specify a username")
                        continue
                    except Exception as e:
                        print(e)
                        continue
                    
                    try:
                        lookup_results = search(username)
                    except Exception as e:
                        print(f"Error: {e}")
                        continue
            
            
            elif prompt[0] == "mtdata":
                if "-h" in prompt:
                    print(mtdata_help_message)
                    continue
                
                try:
                    path = prompt[1]
                    if not os.path.exists(path):
                        print("File doesn't exist")
                        continue
                except: 
                    print("No path specified.")
                    continue
                
                if "-c" in prompt:
                    if "-o" in prompt:
                        out_path = path
                    else:
                        out_path = path.split("/")
                        out_path[-1] = f"modified_{out_path[-1]}"
                        out_path = "/".join(out_path)
                    
                    clear_metadata(path, out_path)
                    
                    mtdata = metadata_extractor(file_path=out_path, check = True)

                    if not mtdata:
                        print("Metadata was cleared successfully!!!")
                else:                    
                    show_mk_note = "-mn" in prompt
                    mtdata = metadata_extractor(file_path=path)
                    
                    if mtdata:
                        for k, v in mtdata.items():
                            if k != "MakerNote" or show_mk_note:
                                print(f"{k}: {v}")
                
                mtdata = {}

            else:
                print("Invalid command")
except KeyboardInterrupt:
    print("\nQuitting...")
