import os, subprocess

options = ['Development kit', 'Gaming kit']
counter = 1

print('What would you like to open:')

for option in options: # Prints all available options
    print(' {}. {}'.format(counter,option))
    counter += 1

prompt_user = '--> '
acceptable = False

while not acceptable:
    user_input = input(prompt_user)
    if user_input == "1":
        print('Opening {}'.format(options[0]))
        subprocess.Popen([r'C:\Users\Austin\AppData\Roaming\Spotify\Spotify.exe']) 
        subprocess.Popen([r'C:\Program Files\Mozilla Firefox\firefox.exe', '-new-tab', 'https://stackoverflow.com/'])
        acceptable = True
    elif user_input == "2":
        print('Opening {}'.format(options[1]))
        subprocess.Popen([r'C:\Users\Austin\AppData\Roaming\Spotify\Spotify.exe', r'C:\Program Files (x86)\Steam\Steam.exe'])
        subprocess.Popen([r'C:\Program Files (x86)\Steam\Steam.exe'])    
        acceptable = True
    else:
        print('You did not enter a valid option')