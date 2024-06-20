# OhShint

Welcome to **OhShint**, a tool designed to aid in OSINT (Open Source Intelligence) investigations. This tool can generate potential usernames and passwords, gather or clear EXIF data from images, and look up potential social media profiles of a username.

## Project Details

This project is hosted on GitHub. For more details, please visit the [OhShint GitHub repository](https://github.com/dxmxtrxs/OhShint).

Contributions, issues, and feature requests are welcome! Feel free to check the repository for the latest updates and to participate in the development.

## Available Commands

- **mtdata**: Extract or clear metadata from an image.
- **user**: Generate a list of possible usernames.
- **pass**: Generate a list of possible passwords.
- **lookup**: Search for a username on different social media sites.
- **show**: Display generated usernames, lookup results, or password list storage path.
- **visit**: Open the webpage of a found URL in a lookup.
- **help**: Display help information about commands or general usage.
- **exit**: Exit the program.

## Setup

1. **Step 1:**
    - Download the latest version of OhShint from the [OhShint GitHub repository](https://github.com/dxmxtrxs/OhShint).
    ```bash
    git clone https://github.com/dxmxtrxs/OhShint.git
    ```

2. **Step 2:**
    - Navigate to the OhShint folder.
    ```bash
    cd /directory/where/ohshint/was/downloaded/at
    ```

3. **Step 3:**
    - Install the requirements.
    ```bash
    pip3 install piexif requests Pillow
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
