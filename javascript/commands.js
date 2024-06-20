// Array of available commands
const availableCommands = ["user", "pass", "lookup spiderman", "mtdata /path/to/image", "mtdata /path/to/image -c -o", "show usernames", "show password", "show lookup", "visit 0", "help", "exit"];
let currentIndex = 0;


// Function to change the command text with fade in and fade out animation
function changeCommand() {
const commandElement = document.querySelector('.command');

setTimeout(() => {
// Change the command text
commandElement.textContent = availableCommands[currentIndex];
currentIndex = (currentIndex + 1) % availableCommands.length;

commandElement.style.opacity = 1; // Fade in

// Check if the current command is "scan"
if (commandElement.textContent === "user") {
    // Update the content of the results span
    const resultsElement = document.querySelector('.results');
    resultsElement.innerHTML = `
What is the name of the target: Master
Enter the last name of the target: Chief
Enter the birthday of the target (DDMMYYYY): 07032511
Would you like to display the created usernames? (y/N): N
Result won't be printed
Enter the name you want the file to be saved as (optional): 
File name was automatically set to: Master_Chief_usernames.txt
File was saved to: /directory/to/save/Master_Chief_usernames.txt
Total usernames generated: 64
`;
} else if (commandElement.textContent === "pass") {
    // Update the content of the results span for sniff command
    const resultsElement = document.querySelector('.results');
    resultsElement.innerHTML = `
What is the name of the target: Bob
Enter the last name of the target: Squarepants
Enter the birthday of the target (DDMMYYYY): 14071986
Enter the name of the targets pet (optional): Gary
Enter the nickname of the target (optional): Spongebob
Enter the size of the wordlist
A) Small (~500 passwords)
B) Medium(~1500 passwords)
C) Large(~14000 passwords)
Note: Sizes vary based on the information given

Selection: B
Enter the name you want the file to be saved as (optional): 
File name was automatically set to: Bob_Squarepants_wordlist.txt
File was saved to: /directory/to/save/Bob_Squarepants_wordlist.txt
Total passwords generated: 1500
`;
} else if (commandElement.textContent === "mtdata /path/to/image") {
    // Update the content of the results span for sniff command
    const resultsElement = document.querySelector('.results');
    resultsElement.innerHTML = `
GPSInfo: {...}
ResolutionUnit: 2
ExifOffset: 228
Make: Apple
Model: iPhone 12
Software: 17.5.1
Orientation: 1
DateTime: 2024:06:16 20:05:07
YCbCrPositioning: 1
XResolution: 72.0
YResolution: 72.0
HostComputer: iPhone 12
...
`;
} else if (commandElement.textContent === "mtdata /path/to/image -c -o") {
    // Update the content of the results span for sniff command
    const resultsElement = document.querySelector('.results');
    resultsElement.innerHTML = `
Metadata was cleared successfully!!!
`;
}else if (commandElement.textContent === "lookup spiderman") {
    // Update the content of the results span for results command
    const resultsElement = document.querySelector('.results');
    resultsElement.innerHTML = `
https://www.instagram.com/spiderman - 200 - OK
Positive match.

https://www.facebook.com/spiderman - 200 - OK
Positive match.

https://www.twitter.com/spiderman - 200 - OK
Positive match.
WARNING: Text has NOT been detected in url, could be a false positive.

https://www.youtube.com/spiderman - 200 - OK
Positive match.

...

FINISHED: A total of X MATCHES found out of Y websites.
`;
} else if (commandElement.textContent === "show usernames") {
    // Check if the ID is 0
    // Update the content of the results span for ID 0
    const resultsElement = document.querySelector('.results');
    resultsElement.innerHTML = `
0: master
1: chief
2: masterchief
3: chiefmaster
4: master.chief
5: chief.master
6: master_chief
7: chief_master
8: mchief
9: masterc
10: m.chief
11: master.c

Username list was stored at:
/directory/to/Master_Chief_usernames.txt
`;
    
} else if (commandElement.textContent === "show password") {
    // Check if the ID is 0
    // Update the content of the results span for ID 0
    const resultsElement = document.querySelector('.results');
    resultsElement.innerHTML = `
Password list was stored at:
/directory/to/Bob_Squarepants_wordlist.txt
`;
    
} else if (commandElement.textContent === "show lookup") {
    // Check if the ID is 0
    // Update the content of the results span for ID 0
    const resultsElement = document.querySelector('.results');
    resultsElement.innerHTML = `
0: https://www.instagram.com/spiderman
1: https://www.facebook.com/spiderman
2: https://www.twitter.com/spiderman
3: https://www.youtube.com/spiderman
...
`;}

else if (commandElement.textContent === "visit 0") {
// Check if the ID is 0
// Update the content of the results span for ID 0
const resultsElement = document.querySelector('.results');
resultsElement.innerHTML = `
Visiting https://www.instagram.com/spiderman...
`;
} else if (commandElement.textContent === "help") {
    // Check if the ID is 0
    // Update the content of the results span for ID 0
    const resultsElement = document.querySelector('.results');
    resultsElement.innerHTML = `
Available Commands:
1. user         - Generate a list of potential usernames
2. pass         - Generate a list of potential passwords
3. lookup       - Search for a username on different social media sites
4. mtdata       - Extract and clear metadata from images
5. show         - Display generated usernames, lookup results, or password list storage path
5. visit        - Open the webpage of a found url in a lookup
6. help         - Display this help message
7. exit         - Exit the program
For more information on a command use: [COMMAND] -h
`;
    
} else if (commandElement.textContent === "exit") {
    // Check if the ID is 0
    // Update the content of the results span for ID 0
    const resultsElement = document.querySelector('.results');
    resultsElement.innerHTML = `
Quitting...
    `;
    
}


}, 500); // 500 milliseconds for the fade out effect
}




// Call the function initially and then every 5 seconds
changeCommand(); // Initial call

setInterval(changeCommand, 5000); // Call every 5 seconds