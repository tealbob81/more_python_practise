from pyfiglet import figlet_format
from colorama import init
from termcolor import colored

init()

valid_colours = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

msg = input('What would you like to print ' )
colour = input('What color? ')
if colour not in valid_colours:
    colour = 'magenta'



art = colored(figlet_format(msg), colour)
print(art)

