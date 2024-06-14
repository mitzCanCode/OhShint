from passwords import generate_passwords
from usernames import generate_usernames
from image_metadata import metadata_extractor, clear_metadata
import os

while True:
        prompt = input("OhShint! > ")
        prompt = prompt.split()
        
        if prompt[0] == "help":
            print("Help message here")
        
        elif prompt[0] == "usr":
            name, last_name, bday = None, None, None
            
            if "-n" in prompt:
                name = prompt[prompt.index("-n") + 1]

            if "-l" in prompt:
                last_name = prompt[prompt.index("-l") + 1]

            if "-b" in prompt:
                bday = prompt[prompt.index("-b") + 1]

            generate_usernames(name, last_name, bday)

        elif prompt[0] == "pass":
            if "-n" in prompt:
                name = prompt[prompt.index("-n") + 1]

            if "-l" in prompt:
                last_name = prompt[prompt.index("-l") + 1]

            if "-b" in prompt:
                bday = prompt[prompt.index("-b") + 1]

            generate_passwords(name, last_name, bday)

        elif prompt[0] == "mtdata":
            if "-h" in prompt:
                print("Usage instructions")
                continue
            
            if "-c" in prompt:
                path = prompt[1]
                if not os.path.exists(path):
                    print("File doesn't exist")
                    continue
                
                mtdata = metadata_extractor(file_path=path)
                
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
                path = prompt[1]
                if not os.path.exists(path):
                    print("File doesn't exist")
                    continue
                
                show_mk_note = "-mn" in prompt
                mtdata = metadata_extractor(file_path=path)
                
                if mtdata:
                    for k, v in mtdata.items():
                        if k != "MakerNote" or show_mk_note:
                            print(f"{k}: {v}")
            
            mtdata = {}

        else:
            print("Invalid command")
