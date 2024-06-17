from passwords import generate_passwords
from usernames import generate_usernames
from image_metadata import metadata_extractor, clear_metadata
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

Examples:
    usr -n Name -l Surname -b 13052000
    usr -l Surname -b 15031969
    usr -N Name -l Surname

"""
pass_help_message = """
Password finder - Generates potential usernames

Usage:
    pass [options]

Options:
    -h             Show this help message
    -n             Name that will be used to generate passwords
    -l             Lastname that will be used to generate passwords
    -b             Birthday that will be used to generate passwords (format: DDMMYYYY)

Examples:
    pass -n Name -l Surname -b 13052000
    pass -l Surname -b 15031969
    pass -N Name -l Surname
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
                name, last_name, bday = None, None, None
                
                if prompt == "usr -h":
                    print(usr_help_message)
                    continue

                if "-n" in prompt:
                    name = prompt[prompt.index("-n") + 1]

                if "-l" in prompt:
                    last_name = prompt[prompt.index("-l") + 1]

                if "-b" in prompt:
                    bday = prompt[prompt.index("-b") + 1]


                generate_usernames(name, last_name, bday)

            elif prompt[0] == "pass":

                if prompt == "pass -h":
                    print(pass_help_message)
                    continue

                if "-n" in prompt:
                    name = prompt[prompt.index("-n") + 1]

                if "-l" in prompt:
                    last_name = prompt[prompt.index("-l") + 1]

                if "-b" in prompt:
                    bday = prompt[prompt.index("-b") + 1]

                generate_passwords(name, last_name, bday)

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
