from colorama import init # used so we can use termcolor without breaking
from termcolor import  colored # to add color to title
import requests # used for http requests
import pyfiglet # asci format title
from random import choice # to choose random joke

init() # from colorama module so we can use termcolor

title = pyfiglet.figlet_format('DAD JOKE 3000!') # set up title
col_title = colored(title, 'blue')
print(col_title)


##res = requests.get(
##    url,
##    headers={'Accept': 'application/json'},
##    params={'term': 'cat', 'limit': 1})
##
##

url = 'https://icanhazdadjoke.com/search' # website to make requests to

msg = input('Please choose a topic for a dad joke: ') # recieve user input

res = requests.get(
    url,
    headers={'Accept': 'application/json'}, # make a query to website using user input as search term
    params={'term': msg}
)
data = res.json() # turn requested data into json format
joke = data['results'] # index of jokes
num_jokes = data['total_jokes'] # how many jokes revieved back from request

if num_jokes > 1:
    print(f'\nThere are {num_jokes} jokes in total. Here is one: ')
    print(f'\n{choice(joke)["joke"]}')
elif num_jokes == 1:
    print('\nThere is one joke')
    print(f"\n{joke[0]['joke']}")
else:
    print("\nSorry I couldn't find a joke with that topic.")
    

#print(f'Here is your joke: \n{joke}')

print('\nThank you using Dad Joke 3000')
