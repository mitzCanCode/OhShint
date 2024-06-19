from passwords import generate_passwords
from usernames import generate_usernames
from image_metadata import metadata_extractor, clear_metadata
from lookup import search
import os
import sys
import time
import webbrowser

ascii_art_lines = [
"              ('-. .-.  .-')    ('-. .-.              .-') _  .-') _          ",
"             ( OO )  / ( OO ). ( OO )  /             ( OO ) )(  OO) )         ",
" .-'),-----. ,--. ,--.(_)---\_),--. ,--.  ,-.-') ,--./ ,--,' /     '._        ",
"( OO'  .-.  '|  | |  |/    _ | |  | |  |  |  |OO)|   \ |  |\ |'--...__)       ",
"/   |  | |  ||   .|  |\  :` `. |   .|  |  |  |  \|    \|  | )'--.  .--'       ",
"\_) |  |\|  ||       | '..`''.)|       |  |  |(_/|  .     |/    |  |          ",
"  \ |  | |  ||  .-.  |.-._)   \|  .-.  | ,|  |_.'|  |\    |     |  |          ",
"   `'  '-'  '|  | |  |\       /|  | |  |(_|  |   |  | \   |     |  |.-..-..-. ",
"     `-----' `--' `--' `-----' `--' `--'  `--'   `--'  `--'     `--'`-'`-'`-' "
]

for line in ascii_art_lines:
    print(f"\033[94m{line}\033[0m")
    time.sleep(0.07)

mtdata_help_message = """
\033[94mmtdata - Metadata extraction and clearing tool\033[0m

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

user_help_message = """
\033[94mUsername generator - Generates potential usernames\033[0m

Usage:
    user 

How to use: 
Just run the command and follow the steps!
"""

pass_help_message = """
\033[94mPassword finder - Generates potential passwords\033[0m

Usage:
    pass 

How to use: 
Just run the command and follow the steps!
"""

lookup_help_message = """
\033[94mLookup - Searches for user information based on a username\033[0m

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

visit_help_message = """
\033[94mVisit - Opens a browser tab of a URL found during a lookup033[0m

Usage:
    visit <id> 

Options:
    -h             Show this help message

Examples:
    visit 0

Notes:
    Before using this command, ensure you have completed a lookup first.

"""

show_help_message = """
\033[94mShow - Displays generated usernames, lookup results, or password list storage path\033[0m

Usage:
    show [options]

Options:
    -h             Show this help message
    usernames      Display the generated usernames
    lookup         Display the results of the lookup
    passwords      Display the path to the stored password list

Notes:
    Before using this command, ensure you have generated usernames, performed a lookup, or generated a password list.
"""

# A function used for openning links found in lookups
def open_website(url):
    webbrowser.open(url)


username_file_path = ""
pass_file_path = ""
lookup_results = {}


try:
    while True:
            prompt = input("OhShint! > ")
            prompt = prompt.split()
            
            if not prompt:
                continue
            
            elif prompt[0] == "exit":
                print("\033[94mQuitting...\033[0m")
                sys.exit()
            elif prompt[0] == "help":
                print("\033[94mAvailable Commands:\033[0m")
                print("\033[94m1. user\t\t- Generate potential usernames\033[0m")
                print("\033[94m2. pass\t\t- Generate potential passwords\033[0m")
                print("\033[94m3. lookup\t- Search for user information based on a username\033[0m")
                print("\033[94m4. mtdata\t- Extract and clear metadata from images\033[0m")
                print("\033[94m5. show\t\t- Display generated usernames, lookup results, or password list storage path\033[0m")
                print("\033[94m5. visit\t\t- Open the webpage of a found url in a lookup\033[0m")
                print("\033[94m6. help\t\t- Display this help message\033[0m")
                print("\033[94m7. exit\t\t- Exit the program\033[0m")          
                print("\033[94mFor more information on a command use: [COMMAND] -h\033[0m")

                continue

            elif prompt[0] == "user":


                name, last_name, bday, prnt, save = None, None, None, False, False
                
                if "-h" in prompt:
                    print(user_help_message)
                    continue
                else: 
                    while True:
                        name = input("What is the name of the target: ")
                        if name == "":
                            print("\033[94mName is not an optional parameter, please enter the targets name\033[0m")
                        elif not name.isalpha():
                            print("\033[94mName should only contain letters\033[0m")
                        else:
                            break

                    while True:
                        last_name = input("Enter the last name of the target: ")
                        if last_name == "":
                            print("\033[94mLast name is not an optional parameter, please enter the targets last name\033[0m")
                        elif not last_name.isalpha():
                            print("\033[94mLast name should only contain letters\033[0m")
                        else:
                            break

                    while True:
                        bday = input("Enter the birthday of the target (DDMMYYYY): ")
                        if bday == "":
                            print("\033[94mBirthday is not an optional parameter, please enter the targets birthdate.\033[0m")
                        elif not bday.isdigit():
                            print("\033[94mBirthday entered contains letters, please enter the birthday in DDMMYYYY format and use only numbers.\033[0m")
                        elif len(bday) != 8:
                            print("\033[94mInvalid birthday format, please enter the birthday in DDMMYYYY format.\033[0m")
                        else:
                            break
                        
                    
                    prnt = input("Would you like to display the created usernames? (y/N): ")
                    try:
                        if prnt == "" or prnt.lower() == "n":
                            prnt = False
                        elif prnt.lower() == "y":
                            prnt = True
                        else:
                            prnt = False
                    except:
                        prnt = False
                            
                    if prnt: print("\033[94mResult will be printed\033[0m")
                    else: print("\033[94mResult won't be printed\033[0m")

                
                    file_name = input("Enter the name you want the file to be saved as (optional): ")
                    if file_name == "":
                        file_name = f"{name}_{last_name}_usernames.txt"
                        print(f"\033[94mFile name was automatically set to: {name}_{last_name}_usernames.txt\033[0m")
                    else: 
                        file_name = file_name + ".txt"


                temp_usernames, username_file_path = generate_usernames(first_name=name, last_name=last_name, bday=bday, file_name=file_name, prnt=prnt)

                usernames = {index: username for index, username in enumerate(temp_usernames)}


            elif prompt[0] == "pass":

                prnt = False
                save = False
                name, last_name, bday, file_name, prnt, save = None, None, None, None, False, False


                if "-h" in prompt:
                    print(pass_help_message)
                    continue


                else:
                    while True:
                        name = input("What is the name of the target: ")
                        if name == "":
                            print("\033[94mName is not an optional parameter, please enter the targets name\033[0m")
                        elif not name.isalpha():
                            print("\033[94mName should only contain letters\033[0m")
                        else:
                            break
                        
                    while True:
                        last_name = input("Enter the last name of the target: ")
                        if last_name == "":
                            print("\033[94mLast name is not an optional parameter, please enter the targets last name\033[0m")
                        elif not last_name.isalpha():
                            print("\033[94mLast name should only contain letters\033[0m")
                        else:
                            break
                    
                    
                        
                    while True:
                        bday = input("Enter the birthday of the target (DDMMYYYY): ")
                        if bday == "":
                            print("\033[94mBirthday is not an optional parameter, please enter the targets birthdate.\033[0m")
                        elif not bday.isdigit():
                            print("\033[94mBirthday entered contains letters, please enter the birthday in DDMMYYYY format and use only numbers.\033[0m")
                        elif len(bday) != 8:
                            print("\033[94mInvalid birthday format, please enter the birthday in DDMMYYYY format.\033[0m")
                        else:
                            break
                        
                    pet = input("Enter the name of the targets pet (optional): ")
                    nickname = input("Enter the nickname of the target (optional): ")
                
                    while True:
                        size = input("Enter the size of the wordlist\nA) Small (~500 passwords)\nB) Medium(~1500 passwords)\nC) Large(~14000 passwords)\nNote: Sizes vary based on the information given\n\nSelection: ")
                        if size == "":
                            print("\033[94mWordlist size is not an optional parameter, please enter the desired size.\033[0m")
                        else:
                            if size.lower() == "a" :
                                size = "small"
                                break
                            elif size.lower() == "b" :
                                size = "medium"
                                break
                            elif size.lower() == "c":
                                size = "large"
                                break
                            else:
                                print("\033[94mInvalid input\033[0m")
                                
                        
                        
                    
                    file_name = input("Enter the name you want the file to be saved as (optional): ")
                    if file_name == "":
                        file_name = f"{name}_{last_name}_wordlist.txt"
                        print(f"\033[94mFile name was automatically set to: {name}_{last_name}_wordlist.txt\033[0m")
                    else: 
                        file_name = file_name + ".txt"


                temp_passwords, pass_file_path = generate_passwords(first_name=name, last_name=last_name, bday=bday, pet=pet, nickname=nickname, file_name=file_name, size=size)
                passwords = {index: password for index, password in enumerate(temp_passwords)}
            
            elif prompt[0] == "show":
                if "-h" in prompt:
                    print(show_help_message)
                    continue
                if "usernames" in prompt:
                    if "usernames" in prompt:
                        for k, v in usernames.items():
                            print(f"{k}: {v}")
                        if username_file_path != "":
                            print(f"\033[94mUsername list was stored at:\n {username_file_path}\033[0m")
                        continue
                    else:
                        print("\033[94mPlease generate a username list first.\033[0m")
                        continue
                elif "lookup" in prompt:
                    if lookup_results:
                        for k, v in lookup_results.items():
                            print(f"{k}: {v}")
                        continue
                    else:
                        print("\033[94mPlease complete a lookup first.\033[0m")
                        continue
                elif "passwords" in prompt:
                    if pass_file_path != "":
                        print(f"\033[94mPassword list was stored at:\n {pass_file_path}\033[0m")
                    else:
                        print("\033[94mPlease generate a password list first\033[0m")
            
            elif prompt[0] == "lookup":
                if "-h" in prompt:
                    print(lookup_help_message)
                    continue
                
                if "-i" in prompt:
                    try:
                        id = prompt[prompt.index("-i") + 1]
                    except IndexError:
                        print("\033[94mPlease specify an ID\033[0m")
                        continue
                    except Exception as e:
                        print(f"\033[94m{e}\033[0m")
                    if not usernames:
                        print("\033[94mGenerate a usernames list to start using IDs\033[0m")
                        continue
                    
                    if not id.isdigit():
                        print("\033[94mID should be a number\033[0m")
                        continue
                    
                    try: 
                        username = usernames[id]
                        print(username)
                    except:
                        print("\033[94mPlease select an ID in the list of usernames generated\033[0m")
                        continue
                    
                    try:
                        lookup_results = search(username)
                    except Exception as e:
                        print(f"\033[94mError: {e}\033[0m")
                        continue
                else:
                    try:
                        username = prompt[1]
                    except IndexError:
                        print("\033[94mPlease specify a username\033[0m")
                        continue
                    except Exception as e:
                        print(f"\033[94m{e}\033[0m")
                        continue
                    
                    try:
                        lookup_results = search(username)
                    except Exception as e:
                        print(f"\033[94mError: {e}\033[0m")
                        continue
            
            
            elif prompt[0] == "visit":
                if "-h" in prompt:
                    print(visit_help_message)
                    continue
                
                try:
                    if lookup_results == {}:
                        print("Please complete a lookup first")
                        continue
                    website_id = prompt[1]
                    if not website_id.isdigit():
                        print("Look up id must be a number")
                        continue
                    else: website_id = int(website_id)
                    if website_id in lookup_results:
                        open_website(lookup_results[website_id])
                        print(f"Visiting {lookup_results[website_id]}...")
                    else:
                        print("Look up ID must be valid, run 'show lookup' to view valid commands")
                except IndexError:
                    print("Please specify an ID")
                except Exception as e:
                    print(e)
                    continue
                    
            
            
            
            elif prompt[0] == "mtdata":
                if "-h" in prompt:
                    print(mtdata_help_message)
                    continue
                
                try:
                    path = prompt[1]
                    if not os.path.exists(path):
                        print("\033[94mFile doesn't exist\033[0m")
                        continue
                except: 
                    print("\033[94mNo path specified.\033[0m")
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
                        print("\033[94mMetadata was cleared successfully!!!\033[0m")
                else:                    
                    show_mk_note = "-mn" in prompt
                    mtdata = metadata_extractor(file_path=path)
                    
                    if mtdata:
                        for k, v in mtdata.items():
                            if k != "MakerNote" or show_mk_note:
                                print(f"\033[94m{k}:\033[0m {v}")
                
                mtdata = {}

            else:
                print("\033[94mInvalid command\033[0m")
except KeyboardInterrupt:
    print("\n\033[94mQuitting...\033[0m")
