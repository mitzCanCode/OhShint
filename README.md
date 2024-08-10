# OhShint

Welcome to **OhShint**, a tool designed to aid in OSINT (Open Source Intelligence) investigations. This tool can generate potential usernames and passwords, gather or clear EXIF data from images, and look up potential social media profiles of a username.

## Project Details

This project is hosted on GitHub. For more details, please visit the [OhShint GitHub repository](https://github.com/mitzCanCode/OhShint).

Contributions, issues, and feature requests are welcome! Feel free to check the repository for the latest updates and to participate in the development.

## Available Commands

- **user**: Generate a list of possible usernames.
- **pass**: Generate a list of possible passwords.
- **lookup**: Search for a username on different social media sites.
- **mtdata**: Extract or clear metadata from an image.
- **email**: Generate a list of potential emails.
- **ip**: Get details about an IP address.
- **url**: Get IP details from a given URL.
- **visit**: Open the webpage of a found URL in a lookup.
- **show**: Display generated usernames, lookup results, or password list storage path.
- **help**: Display help information about commands or general usage.
- **exit**: Exit the program.

## Setup

1. **Step 1:**
    - Download the latest version of OhShint from the [OhShint GitHub repository](https://github.com/mitzCanCode/OhShint).
    ```bash
    git clone https://github.com/mitzCanCode/OhShint.git
    ```

2. **Step 2:**
    - Navigate to the OhShint folder.
    ```bash
    cd /directory/where/ohshint/was/downloaded/at
    ```

3. **Step 3:**
    - Install the requirements.
    ```bash
    pip3 install piexif requests Pillow ip2geotools geopy requests
    ```

## How to Use

1. **Step 1:**
    - Start the script.
    ```bash
    python3 OhShint.py
    ```

2. **Step 2:**
    - Start searching!
    ```bash
    OhShint> command
    ```

## Notes

- The script is stable on macOS but hasn't been tested on other operating systems yet.

## Disclaimer

This is a project made for fun and should not be used in the real-world. We are not liable for any damage caused by the user.
