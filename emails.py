from usernames import generate_usernames
import os

def generate_emails(first_name: str = "", last_name: str = "", bday: str = "", tld: list = [], domain: list = [], file_name: str = "", prnt: bool = True) -> list:
    possible_emails = []
    possible_usernames, _ = generate_usernames(first_name = first_name, last_name = last_name, bday = bday, save = False)
    common_tlds = [
    "com", "org", "net", "edu", "gov", "mil", "int",
    "co", "us", "uk", "de", "jp", "fr", "au", "ca",
    "eu", "ru", "cn", "br", "in", "gr", "dev", "app"
    ]

    common_domains = [
    "gmail", "yahoo", "outlook", "hotmail", "icloud", 
    "aol", "protonmail", "zoho", "mail", "yandex", 
    "gmx", "inbox", "fastmail", "riseup", "tutanota", 
    "lavabit", "hushmail", "runbox", "mail"
    ]

    if not tld:
        tld_to_use = common_tlds
    else:
        tld_to_use = tld
    
    if not domain:
        domain_to_use = common_domains
    else:
        domain_to_use = domain

    for username in possible_usernames:
        for domain in domain_to_use:
            for tld in tld_to_use:
                possible_emails.append(f"{username}@{domain}.{tld}")

    with open(file_name, "w") as f:
        for i in range(len(possible_emails)):
            if prnt:
                print(f"\033[94m{i}. {possible_emails[i]}\033[0m")
            f.write(possible_emails[i] + "\n")
        f.write(f"\nTotal emails generated: {len(possible_emails)}")
        file_path = os.path.abspath(file_name)
        print(f"\033[94mFile was saved to: {file_path}\033[0m")
        print(f"\033[94mTotal emails generated: {len(possible_emails)}\033[0m")

    return possible_emails, file_path

if __name__ == "__main__":
    generate_emails(first_name = "name", last_name = "surname", bday = "12345678", tld = ["com", "org"], domain = [], file_name = "sample_emails.txt", prnt = True)

