# NOTE PATHS TO PROGRAMS WILL DIFFER PER USER

import os, subprocess

counter = 1
options = ['Development kit', 'Gaming kit'] # Available kits to open

print('What would you like to open:')

for option in options: # Prints all available options
    print(' {}. {}'.format(counter,option))
    counter += 1

prompt_user = '--> '
acceptable_input = False

while not acceptable_input:
    user_input = input(prompt_user)
    if user_input == "1": # Open spotify and firefox with stack overflow
                          # PATHS TO PROGRAMS WILL DIFFER PER USER
        print('Opening {}'.format(options[0]))
        subprocess.Popen([r'C:\Users\Austin\AppData\Roaming\Spotify\Spotify.exe']) 
        subprocess.Popen([r'C:\Program Files\Mozilla Firefox\firefox.exe', '-new-tab', 'https://stackoverflow.com/'])
        acceptable_input = True
    elif user_input == "2":
        print('Opening {}'.format(options[1])) # Open spotify and steam
        subprocess.Popen([r'C:\Users\Austin\AppData\Roaming\Spotify\Spotify.exe', r'C:\Program Files (x86)\Steam\Steam.exe'])
        subprocess.Popen([r'C:\Program Files (x86)\Steam\Steam.exe'])    
        acceptable_input = True
    else:
        print('You did not enter a valid option')