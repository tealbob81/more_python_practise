import requests

##
##
###print(res.text)
##data = res.json()
##print(data['joke'])
##
##help(requests.get)

url = 'https://icanhazdadjoke.com/search'
res = requests.get(
    url,
    headers={'Accept': 'application/json'},
    params={'term': 'cat', 'limit': 1})

data = res.json()
print(data['results'])
